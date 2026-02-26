# MLOps Pipeline - Cryptocurrency Signal Generator

This project implements the Round-0 technical assessment pipeline.
It runs deterministically from `config.yaml`, processes OHLCV data from `data.csv`,
computes rolling mean signals, writes structured metrics JSON, and logs full execution.
Rolling mean uses `min_periods=1`, so the first `window-1` rows are computed from the available prefix.

## Setup Instructions

```bash
pip install -r requirements.txt
```

## Local Execution Instructions

```bash
python run.py --input data.csv --config config.yaml \
              --output metrics.json --log-file run.log
```

## Docker Instructions

```bash
docker build -t mlops-task .
docker run --rm mlops-task
```

## Expected Output

`metrics.json` (success example):

```json
{
  "version": "v1",
  "rows_processed": 10000,
  "metric": "signal_rate",
  "value": 0.4977,
  "latency_ms": 16,
  "seed": 42,
  "status": "success"
}
```

Error output format:

```json
{
  "version": "v1",
  "status": "error",
  "error_message": "Description of what went wrong"
}
```

## Dependencies

- pandas==2.0.3
- numpy==1.24.4
- pyyaml==6.0.1

## Notes

- Config fields in `config.yaml`: `seed`, `window`, `version`
- Validation requires readable non-empty input and mandatory `close` column
- Exit code: `0` on success, non-zero on failure
- Required deliverables included: `run.py`, `config.yaml`, `data.csv`, `requirements.txt`, `Dockerfile`, `README.md`, `metrics.json`, `run.log`
