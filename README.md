# MLOps Internship Task 0 – Batch Signal Generator

**Author:** Uwais Abdul Kalam Chaudhary  
**Date:** June 3, 2026  
**Target:** MetaStackerBandit Internship Assessment (Primetrade.ai)

---

## Overview

This repository contains a production-ready, containerized Python batch-processing pipeline designed to ingest financial OHLCV (Open, High, Low, Close, Volume) data and compute deterministic binary trading signals. The project is engineered from the ground up to meet strict production-level requirements for **reproducibility**, **observability**, and **deployment readiness**.

### Core Features
* **Environment Isolation:** Fully containerized using Docker to guarantee identical execution across local and cloud environments.
* **Structured Observability:** Robust runtime tracking utilizing Python's native logging framework.
* **Automated Metrics Collection:** Generates structured execution metadata (latency, row count, status) in JSON format for easy downstream ingestion by monitoring tools.
* **Flexible Configuration:** Dynamic pipeline behavior driven entirely by externalized YAML configuration files.

---

## Repository Structure

```text
.
├── run.py              # Main execution script / CLI entrypoint
├── requirements.txt    # Python dependencies
├── Dockerfile          # Multi-stage/minimal container definition
├── config.yaml         # Pipeline parameters and signal thresholds
├── data.csv            # Input OHLCV financial dataset
├── metrics.json        # Output telemetry and execution performance (Generated)
├── run.log             # Application execution logs (Generated)
└── README.md           # Documentation
