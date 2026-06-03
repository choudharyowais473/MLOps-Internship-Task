# MLOps Internship Task 0 – Batch Signal Generator

**[span_0](start_span)Author:** Uwais Abdul Kalam Chaudhary[span_0](end_span)  
**[span_1](start_span)Date:** June 3, 2026[span_1](end_span)  
**[span_2](start_span)Target:** MetaStackerBandit Technical Assessment (Primetrade.ai)[span_2](end_span)

---

## Overview

[span_3](start_span)This repository contains a production-ready, containerized Python batch job that demonstrates foundational MLOps principles: **reproducibility**, **structured observability**, and **deployment readiness**[span_3](end_span). 

[span_4](start_span)The pipeline ingests a 10,000-row financial OHLCV dataset (`data.csv`), dynamically configures parameter settings via YAML, validates data structures, computes a rolling mean on the `close` metric, and generates a binary trading signal[span_4](end_span). 

### Core Specifications Implemented
* **[span_5](start_span)[span_6](start_span)Determinism:** Pipeline execution seeds the underlying pseudo-random number generator frameworks using parameters defined in the configuration[span_5](end_span)[span_6](end_span).
* **[span_7](start_span)Strict Validation:** Active runtime exception handling for missing inputs, empty files, incorrect formats, or absent target columns (`close`)[span_7](end_span).
* **[span_8](start_span)[span_9](start_span)Dual Execution:** Runs natively as a modular CLI utility or as an isolated container passing strict evaluation tests[span_8](end_span)[span_9](end_span).

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
└── README.md           # Documentation
