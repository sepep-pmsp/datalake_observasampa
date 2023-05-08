import sys
sys.path.append("/opt/airflow")

from os.path import join
import argparse
import os
import json
import shutil
from core.minio import MinIO

import pandas as pd
from sqlalchemy.engine import create_engine

from datetime import datetime

def export_to_trino(engine, df, table_name, dest):
    return df.to_sql(name=table_name, con=engine, schema=dest, method="multi", index=False, if_exists='append')


def twitter_transformation_pandas(engine, src, dest, process_date):
    process_date_dt = datetime.strptime(process_date, '%Y-%m-%d')

    minio = MinIO(config={'NAME': 'minio', 'S3_HOST': 'minio', 'S3_PORT': '9000',
                          'S3_ACCESS_KEY': os.getenv("MINIO_ROOT_USER"),
                          'S3_SECRET_KEY': os.getenv("MINIO_ROOT_PASSWORD")})

    response_data = minio.getObj("bronze", src)
    json_str = response_data.decode('utf-8')
    df = pd.read_json(json_str)
    tweets_list = (df['data'][0])
    tweets_df = pd.DataFrame(tweets_list)
    tweets_df['process_date'] = process_date_dt

    users_list = (df['includes'][0]['users'])
    users_df = pd.DataFrame(users_list)
    users_df['process_date'] = process_date_dt

    public_metrics = []
    for i in pd.DataFrame(tweets_df['public_metrics']).itertuples():
        public_metrics.append(i.public_metrics)

    public_metrics_df = pd.DataFrame(public_metrics)
    public_metrics_df['id'] = tweets_df['id']
    public_metrics_df['process_date'] = process_date_dt

    tweets_df = tweets_df.drop(['public_metrics', 'edit_history_tweet_ids'], axis='columns')

    dest_a = dest.split('.')
    dest_b = dest.replace(dest_a[0] + '.', '') + '_'

    export_to_trino(engine, tweets_df, dest_b + 'tweets', dest_a[0])
    export_to_trino(engine, users_df, dest_b + 'users', dest_a[0])
    export_to_trino(engine, public_metrics_df, dest_b + 'public_metrics', dest_a[0])


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Spark Twitter Transformation",
    )
    parser.add_argument("--src", required=True)
    parser.add_argument("--dest", required=True)
    parser.add_argument("--process_date", required=True)
    args = parser.parse_args()

    host_trino = os.getenv("TRINO_HOST")
    port_trino = os.getenv("TRINO_PORT")
    db_trino = os.getenv("TRINO_DB")
    user_trino = os.getenv("TRINO_USER")
    url_trino = 'trino://{host}:{port}/{data_base}/'
    engine = create_engine(
        url_trino.format(host=host_trino, port=port_trino, data_base=db_trino),
        connect_args={'user': user_trino},
    )

    twitter_transformation_pandas(engine, args.src, args.dest, args.process_date)
