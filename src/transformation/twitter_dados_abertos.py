import sys
sys.path.append("/opt/airflow")

import argparse
import os
# import json

import pandas as pd
from core.minio import MinIO
from core.trino import TrinoSQLAlchemy
from datetime import datetime

def twitter_transformation_pandas(src, dest, process_date):
    process_date_dt = datetime.strptime(process_date, '%Y-%m-%d')

    minio = MinIO(config={'NAME': 'minio', 'S3_HOST': 'minio', 'S3_PORT': '9000',
                          'S3_ACCESS_KEY': os.getenv("MINIO_ACCESS_KEY"),
                          'S3_SECRET_KEY': os.getenv("MINIO_SECRET_KEY")})

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

    trino = TrinoSQLAlchemy(config={'TRINO_HOST': os.getenv("TRINO_HOST"),
                                    'TRINO_PORT': os.getenv("TRINO_PORT"),
                                    'TRINO_DB': os.getenv("TRINO_DB"),
                                    'TRINO_USER': os.getenv("TRINO_USER")})

    trino.export_to_trino(df=tweets_df, table_name=dest_b + 'tweets', dest=dest_a[0],
                          method="multi", index=False, if_exists='append')
    trino.export_to_trino(df=users_df, table_name=dest_b + 'users', dest=dest_a[0],
                          method="multi", index=False, if_exists='append')
    trino.export_to_trino(df=public_metrics_df, table_name=dest_b + 'public_metrics',
                          dest=dest_a[0], method="multi", index=False, if_exists='append')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Spark Twitter Transformation",
    )
    parser.add_argument("--src", required=True)
    parser.add_argument("--dest", required=True)
    parser.add_argument("--process_date", required=True)
    args = parser.parse_args()

    twitter_transformation_pandas(args.src, args.dest, args.process_date)
