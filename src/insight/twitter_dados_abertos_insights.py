import sys
sys.path.append("/opt/airflow")

import argparse
import os
import pandas as pd

from core.trino import TrinoSQLAlchemy
# from sqlalchemy import create_engine
from datetime import datetime

# def get_engine_trino():
#     host_trino = os.getenv("TRINO_HOST")
#     port_trino = os.getenv("TRINO_PORT")
#     db_trino = os.getenv("TRINO_DB")
#     user_trino = os.getenv("TRINO_USER")
#     url_trino = 'trino://{host}:{port}/{data_base}/'
#     engine = create_engine(
#         url_trino.format(host=host_trino, port=port_trino, data_base=db_trino),
#         connect_args={'user': user_trino},
#     )
#     return engine
#
#
# def trino_read_tables(src, table_name):
#     engine = get_engine_trino()
#     connection = engine.connect()
#     db_trino = os.getenv("TRINO_DB")
#     query = "SELECT * FROM {db}.{src}.{table_name}".format(db=db_trino, src=src, table_name=table_name)
#     return pd.read_sql(query, connection)
#
#
# def export_to_trino(df, table_name, dest):
#     engine = get_engine_trino()
#     print(table_name)
#     print(dest)
#     print(df)
#     return df.to_sql(name=table_name, con=engine, schema=dest, method="multi", index=False, if_exists='append')


def twitter_insights_pandas(src, dest, process_date):
    trino = TrinoSQLAlchemy(config={'TRINO_HOST': os.getenv("TRINO_HOST"),
                                    'TRINO_PORT': os.getenv("TRINO_PORT"),
                                    'TRINO_DB': os.getenv("TRINO_DB"),
                                    'TRINO_USER': os.getenv("TRINO_USER")})

    df_users = trino.trino_read_tables(src, 'twitter_dados_abertos_users')
    df_tweets = trino.trino_read_tables(src, 'twitter_dados_abertos_tweets')
    df_public_metrics = trino.trino_read_tables(src, 'twitter_dados_abertos_public_metrics')

    df_authors = df_tweets.groupby("author_id").agg(
        {"author_id": pd.Series.nunique})

    process_date_dt = datetime.strptime(process_date, '%Y-%m-%d')
    df_authors['process_date'] = process_date_dt
    trino.export_to_trino(df=df_authors, table_name='twitter_dados_abertos_authors',
                          dest=dest, method="multi", index=False, if_exists='append')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Spark Twitter Transformation",
    )
    parser.add_argument("--src", required=True)
    parser.add_argument("--dest", required=True)
    parser.add_argument("--process_date", required=True)
    args = parser.parse_args()

    twitter_insights_pandas(args.src, args.dest, args.process_date)
