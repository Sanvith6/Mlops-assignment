import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OHLCV signal generation pipeline")
    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file",
    )
    parser.add_argument(
        "--config",
        required=True,
        help="Path to YAML config file",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path for output metrics JSON",
    )
    parser.add_argument(
        "--log-file",
        required=True,
        dest="log_file",
        help="Path for log file",
    )
    return parser.parse_args()
