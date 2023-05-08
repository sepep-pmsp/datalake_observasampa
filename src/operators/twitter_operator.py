import sys
from os.path import join
# from pathlib import Path

sys.path.append("/opt/airflow")

from datetime import datetime, timedelta
from airflow.models import BaseOperator, DAG, TaskInstance
from src.hooks.twitter_hook import TwitterHook
import os

class TwitterOperator(BaseOperator):

    template_fields = ["query", "file_path", "start_time", "end_time"]

    def __init__(self, stage, file_path, end_time, start_time, query, **kwargs):
        self.end_time = end_time
        self.start_time = start_time
        self.query = query
        self.file_path = file_path
        self.stage = stage
        super().__init__(**kwargs)

    def dump_data_to_bucket(self, tweet_list: list):

        import pandas as pd
        from minio import Minio
        from io import BytesIO

        # MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")
        MINIO_BUCKET_NAME = self.stage
        MINIO_ROOT_USER = os.getenv("MINIO_ACCESS_KEY")
        MINIO_ROOT_PASSWORD = os.getenv("MINIO_SECRET_KEY")

        df = pd.DataFrame(tweet_list)
        json = df.to_json(force_ascii=False).encode("utf-8")

        client = Minio("minio:9000", access_key=MINIO_ROOT_USER, secret_key=MINIO_ROOT_PASSWORD, secure=False)

        # Make MINIO_BUCKET_NAME if not exist.
        found = client.bucket_exists(MINIO_BUCKET_NAME)
        if not found:
            client.make_bucket(MINIO_BUCKET_NAME)
        else:
            print(f"Bucket '{MINIO_BUCKET_NAME}' already exists!")

        # Put json data in the bucket
        client.put_object(
            MINIO_BUCKET_NAME, self.file_path, data=BytesIO(json), length=len(json), content_type="application/json")

    def execute(self, context):
        end_time = self.end_time
        start_time = self.start_time
        query = self.query

        tweet_list = []

        for pg in TwitterHook(end_time, start_time, query).run():
            tweet_list.append(pg)

        self.dump_data_to_bucket(tweet_list)


if __name__ == "__main__":
    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"
    end_time = (datetime.now() + timedelta(-1)).strftime(TIMESTAMP_FORMAT)
    start_time = (datetime.now() + timedelta(-2)).date().strftime(TIMESTAMP_FORMAT)
    query = "smit"

    with DAG(dag_id = "TwitterTest", start_date=datetime.now()) as dag:
        to = TwitterOperator(file_path=join("/opt/airflow/datalake/twitter_datascience",
                                            f"extract_date={datetime.now().date()}",
                                            f"datascience_{datetime.now().date().strftime('%Y%m%d')}.json"),
            query=query,
            start_time=start_time,
            end_time=end_time,
            task_id="test_run")
        ti = TaskInstance(task=to)
        to.execute(ti.task_id)


