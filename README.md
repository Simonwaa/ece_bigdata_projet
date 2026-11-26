# Big Data project – <TITLE>

## Authors

- LASTNAME Firstname

## Prerequisites

- An Onyxia account with S3 access (namespace: `user-<onyxia-id>`)
- An Onyxia service with Python 3.x (e.g. VSCode-python / Jupyter-python), which injects the S3 credentials as environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `AWS_S3_ENDPOINT`)
- `pip install -r requirements.txt`
- *(if applicable)* `kubectl` access to the namespace, for the manifests in `k8s/`

## Dataset

| Field | Value |
|---|---|
| Name | <dataset name> |
| URL | <url> |
| License | <license> |
| Download date | <YYYY-MM-DD> |
| Size (raw) | <x.x MB>, must be between 1 and 5 MB |

## Problem statement

<At most 3 sentences: the question, what is measured, and the verifiable result expected.>

## S3 paths

| Data | Path |
|---|---|
| Raw | `s3://<bucket>/bigdata_project/raw/` |
| Processed | `s3://<bucket>/bigdata_project/processed/` |
| Final | `s3://<bucket>/bigdata_project/final/` |

## Reproduction

```bash
# 0. Clone the repo and install the dependencies (in an Onyxia service)
git clone https://github.com/Simonwaa/ece_bigdata_projet.git && cd ece_bigdata_projet
pip install -r requirements.txt

# 1. Download the raw data and upload it to S3
python src/ingest/<script>.py

# 2. Run the processing
python src/processing/<script>.py

# 3. Check the result independently
python src/verification/<script>.py
```

**Restart:** every step reads its input from S3 and overwrites its output, so any step can be rerun on its own.

## Repository layout

```text
├── README.md
├── evidence/   # numbered screenshots 01_..., 02_... (Onyxia ID and date visible)
├── src/        # all code: ingest/, processing/, verification/
└── k8s/        # Kubernetes manifests, if applicable
```
