# MLOps Pipeline — Cryptocurrency Signal Generator

A lightweight batch pipeline that processes OHLCV cryptocurrency data, computes a rolling mean on closing prices, and generates a binary trading signal. Built as a reproducible, Dockerised MLOps job with structured logging and JSON metrics output.

---

## How it works

For each row in the dataset:
1. Compute the rolling mean of `close` over the last N periods (configurable via `window`)
2. Assign `signal = 1` if `close > rolling_mean`, else `signal = 0`
3. Report the proportion of 1s as `signal_rate`

---

## Project structure

```
.
├── main.py           # Pipeline orchestration entrypoint
â”œâ”€â”€ run.py            # Backward-compatible wrapper entrypoint
â”œâ”€â”€ cli.py            # CLI argument parsing
â”œâ”€â”€ logger_utils.py   # Logger setup
â”œâ”€â”€ config_loader.py  # YAML config loading/validation
â”œâ”€â”€ data_loader.py    # CSV loading/validation
â”œâ”€â”€ signal_processor.py# Rolling mean + signal computation
â”œâ”€â”€ metrics_writer.py # Metrics JSON output
├── config.yaml       # Job configuration
├── data.csv          # Input dataset (10,000 rows of BTC OHLCV)
├── requirements.txt  # Python dependencies
├── Dockerfile        # Container definition
├── metrics.json      # Example output from a successful run
├── run.log           # Example log from a successful run
└── README.md
```

---

## Setup Instructions

```bash
# Install dependencies
pip install -r requirements.txt
```

---

## Local Execution Instructions

```bash
# Run locally
python run.py --input data.csv --config config.yaml \
              --output metrics.json --log-file run.log
```

---

## Docker Instructions

```bash
# Build the Docker image
docker build -t mlops-task .

# Run the container
docker run --rm mlops-task
```

---

## Expected Output

`metrics.json`:

```json
{
  "version": "v1",
  "rows_processed": 10000,
  "metric": "signal_rate",
  "value": 0.4977,
  "latency_ms": 22,
  "seed": 42,
  "status": "success"
}
```

On failure:

```json
{
  "version": "v1",
  "status": "error",
  "error_message": "Description of what went wrong"
}
```

---

## Configuration

`config.yaml` controls all pipeline parameters — no hard-coded values in the code.

| Field   | Type   | Description                                     |
|---------|--------|-------------------------------------------------|
| seed    | int    | Random seed — ensures identical results every run |
| window  | int    | Rolling window size for mean calculation        |
| version | string | Version tag written into the metrics output     |

---

## Dependencies

| Package | Version |
|---------|---------|
| pandas  | 2.0.3   |
| numpy   | 1.24.4  |
| pyyaml  | 6.0.1   |

---

## Error handling

The pipeline handles all failure cases gracefully and writes a structured error JSON instead of crashing:

- Missing input file
- Invalid or unreadable CSV
- Empty CSV file
- Missing required columns (`timestamp`, `open`, `high`, `low`, `close`)
- Missing or malformed config file

Exit code is `0` on success, `1` on any error.
