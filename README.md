# MLOps Batch Job — Task 0

A minimal MLOps-style batch pipeline that loads OHLCV data, computes a rolling mean signal, and outputs structured metrics with full logging.

---

## Project Structure

```
.
├── run.py
├── config.yaml
├── data.csv
├── requirements.txt
├── Dockerfile
├── metrics.json
├── run.log
└── README.md
```

---

## Local Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the pipeline

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

No hard-coded paths — all files are passed via CLI flags.

---

## Docker Build & Run

### Build

```bash
docker build -t mlops-task .
```

### Run

```bash
docker run --rm mlops-task
```

The container includes `data.csv` and `config.yaml`, writes `metrics.json` and `run.log` internally, and prints the final metrics JSON to stdout.

- Exit code `0` → success  
- Non-zero exit code → failure

---

## Config (`config.yaml`)

```yaml
seed: 42
window: 5
version: "v1"
```

| Field | Description |
|-------|-------------|
| `seed` | NumPy random seed for reproducibility |
| `window` | Rolling mean window size |
| `version` | Pipeline version tag written to output |

---

## Example Output (`metrics.json`)

```json
{
  "version": "v1",
  "rows_processed": 10000,
  "metric": "signal_rate",
  "value": 0.4990,
  "latency_ms": 127,
  "seed": 42,
  "status": "success"
}
```

### Error case

```json
{
  "version": "v1",
  "status": "error",
  "error_message": "Missing required column: close"
}
```

Metrics are written in **both** success and error cases.

---

## Signal Logic

- Rolling mean computed on the `close` column using the configured `window`
- First `window - 1` rows produce NaN rolling mean and are **excluded** from signal computation
- `signal = 1` if `close > rolling_mean`, else `signal = 0`
- `signal_rate = mean(signal)` over all valid (non-NaN) rows

---

## Reproducibility

Results are fully deterministic given the same `config.yaml` and `data.csv`. The seed is set via `numpy.random.seed(seed)` at job start.
