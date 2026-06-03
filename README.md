# MLOps-Internship-Task
Containerized ML batch job for trading signal generation – MLOps internship task
# MLOps Internship Task 0 – Batch Signal Generator

**Author:** Uwais Abdul Kalam Chaudhary  
**Date:** June 3, 2026  

This repository contains a containerized Python batch job that computes a binary trading signal from OHLCV data. It meets the reproducibility, observability, and deployment‑readiness requirements of the MetaStackerBandit internship assessment.

## Requirements

- Python 3.9+
- Docker (for containerized runs)
- Python packages listed in `requirements.txt`: `pandas`, `numpy`, `pyyaml`

## Local Run (without Docker)

1. Clone the repository and navigate to the project folder.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
## Docker Build & Run
docker build -t mlops-task .
docker run --rm -v $(pwd):/app mlops-task --input data.csv --config config.yaml --output /app/metrics.json --log-file /app/run.log