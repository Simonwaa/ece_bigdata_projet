"""S3 access shared by every step. Uses the credentials that Onyxia injects into the service."""
import os

import s3fs

BUCKET = os.environ.get("S3_BUCKET", "<onyxia-id>")  # personal bucket = Onyxia user name
PREFIX = f"{BUCKET}/bigdata_project"
RAW = f"{PREFIX}/raw"
PROCESSED = f"{PREFIX}/processed"
FINAL = f"{PREFIX}/final"


def get_fs() -> s3fs.S3FileSystem:
    return s3fs.S3FileSystem(
        client_kwargs={"endpoint_url": "https://" + os.environ["AWS_S3_ENDPOINT"]},
        key=os.environ["AWS_ACCESS_KEY_ID"],
        secret=os.environ["AWS_SECRET_ACCESS_KEY"],
        token=os.environ.get("AWS_SESSION_TOKEN"),
    )
