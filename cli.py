import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OHLCV signal generation pipeline")
    parser.add_argument(
        "--input",
        default="data.csv",
        help="Path to input CSV file (default: data.csv)",
    )
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to YAML config file (default: config.yaml)",
    )
    parser.add_argument(
        "--output",
        default="metrics.json",
        help="Path for output metrics JSON (default: metrics.json)",
    )
    parser.add_argument(
        "--log-file",
        default="run.log",
        dest="log_file",
        help="Path for log file (default: run.log)",
    )
    return parser.parse_args()
