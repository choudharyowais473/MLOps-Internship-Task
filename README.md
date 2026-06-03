# MLOps Internship Task 0 – Batch Signal Generator

**Author:** Uwais Abdul Kalam Chaudhary  
**Date:** June 3, 2026  
**Target:** MetaStackerBandit Technical Assessment (Primetrade.ai)

---

## Overview

This repository contains a production-ready, containerized Python batch job that demonstrates foundational MLOps principles: **reproducibility**, **structured observability**, and **deployment readiness**[span_0](start_span)[span_0](end_span). 

The pipeline ingests a 10,000-row financial OHLCV dataset (`data.csv`), dynamically configures parameter settings via YAML, validates data structures, computes a rolling mean on the `close` metric, and generates a binary trading signal. 

### Core Specifications Implemented
* **Determinism:** Pipeline execution seeds the underlying pseudo-random number generator frameworks using parameters defined in the configuration[span_1](start_span)[span_1](end_span).
* **Strict Validation:** Active runtime exception handling for missing inputs, empty files, incorrect formats, or absent target columns (`close`).
* **Dual Execution:** Runs natively as a modular CLI utility or as an isolated container passing strict evaluation tests.

---

## Repository Structure

```text
.
├── run.py              # Core application code & command-line interface
├── requirements.txt    # Application dependencies (pandas, numpy, pyyaml)
├── Dockerfile          # Configuration for building reproducible image
├── config.yaml         # Configuration file setting seed, window size, and version
├── data.csv            # Input OHLCV file (10,000 rows for analysis)
├── metrics.json        # Machine-readable telemetry file (Generated on execution)
├── run.log             # Detailed application log (Generated on execution)
└── README.md           #Documentation
##Local Run (Development Environment)
​The pipeline is implemented as a strict CLI application with no hard-coded paths. Use the required flags to supply inputs and target output file destinations.

# 1. Install required packages
pip install -r requirements.txt

# 2. Run the program with explicit CLI arguments
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log

## Docker Run (Production & Evaluation)
​The containerization strategy supports automated evaluation orchestration. The configuration and data assets are self-contained within the image, and a valid execution outputs metrics to stdout while writing artifacts to disk.
​To build and run the pipeline exactly as performed during evaluation, execute:

# 1. Build the Docker image
docker build -t mlops-task .

# 2. Execute the containerized batch job
docker run --rm mlops-task
## Architecture and Data Contracts

Configuration Strategy (config.yaml)
​Pipeline configuration is fully decoupled from the core execution engine and strictly enforces the following schema parameters:

version: "v1"
seed: 42
window: 5

## Pipeline Signal Logic

​Validation: Checks if the data file exists, contains a non-empty layout, is formatted as a valid CSV, and exposes the target column close.
​Rolling Mean: Computes the moving window average over the configured window size. First window - 1 rows are handled consistently as NaN values and excluded from metrics aggregation to avoid data leakage.
​Signal Generation: Implements deterministic evaluation logic per row:
​signal = 1 if close > rolling_mean
​signal = 0 otherwise
##Observability & Artifact Schemas
​The pipeline explicitly generates and updates the metrics telemetry file in both success and error execution outcomes.
​Sample Success Output (metrics.json)
{
    "version": "v1",
    "rows_processed": 10000,
    "metric": "signal_rate",
    "value": 0.4990,
    "latency_ms": 127,
    "seed": 42,
    "status": "success"
}

Sample Error Output (metrics.json)
##Logging Flow (run.log)
​System operations use standard logging layers mapping to key processing milestones:
​Job Start: Captures precise baseline timestamp initialization.
​Configuration Step: Tracks file deserialization and confirms keys (seed, window, version).
​Ingestion Metrics: Outputs exact counts of lines loaded into memory.
​Transformations: Confirms computing metrics across rolling averages and structural checks.
​Telemetry Dump: Echoes structural evaluation metrics summarizing data parameters.
​Job Termination: Tracks termination runtime metrics and explicit error logging where relevant.
## Pipeline Exit Codes
​Integrates natively with automated CI/CD orchestrators, job schedulers, and evaluation validation platforms:
​0 — Success: Data validated, signals computed, and all target artifacts exported cleanly.
​Non-zero — Failure: An error or validation anomaly triggered a termination sequence. Detailed debugging information is redirected to run.log.

