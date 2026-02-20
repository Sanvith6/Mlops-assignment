import sys
import time

import numpy as np

from cli import parse_args
from config_loader import load_config
from data_loader import load_data
from logger_utils import get_logger
from metrics_writer import write_metrics
from signal_processor import compute_signals


def main() -> int:
    args = parse_args()
    start_time = time.time()

    log = get_logger(args.log_file)
    log.info("Job started")

    version = "v1"

    try:
        cfg = load_config(args.config)
        seed, window, version = cfg["seed"], cfg["window"], cfg["version"]
        np.random.seed(seed)
        log.info(f"Config loaded: seed={seed}, window={window}, version={version}")

        df = load_data(args.input)
        log.info(f"Data loaded: {len(df)} rows")

        _, signals = compute_signals(df, window)
        log.info(f"Rolling mean calculated with window={window}")
        log.info("Signals generated")

        rows_processed = len(df)
        signal_rate = round(float(signals.mean()), 4)
        latency_ms = int((time.time() - start_time) * 1000)

        log.info(f"Metrics: signal_rate={signal_rate}, rows_processed={rows_processed}")
        log.info(f"Job completed successfully in {latency_ms}ms")

        payload = {
            "version": version,
            "rows_processed": rows_processed,
            "metric": "signal_rate",
            "value": signal_rate,
            "latency_ms": latency_ms,
            "seed": seed,
            "status": "success",
        }
        write_metrics(args.output, payload)
        return 0

    except Exception as exc:
        latency_ms = int((time.time() - start_time) * 1000)
        log.error(f"Pipeline error: {exc}")
        log.info(f"Job completed with errors in {latency_ms}ms")

        payload = {
            "version": version,
            "status": "error",
            "error_message": str(exc),
        }
        write_metrics(args.output, payload)
        return 1


if __name__ == "__main__":
    sys.exit(main())
