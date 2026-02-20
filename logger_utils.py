import logging
import sys


def get_logger(log_path: str) -> logging.Logger:
    logger = logging.getLogger("pipeline")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        logger.handlers.clear()

    fmt = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    fh = logging.FileHandler(log_path, mode="w")
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    return logger
