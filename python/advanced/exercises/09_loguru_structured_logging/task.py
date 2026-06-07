"""Exercise starter for lesson: 09_loguru_structured_logging."""
from __future__ import annotations

import json
import logging
import sys
from pathlib import Path


def configure_logger() -> logging.Logger:
    log_dir = Path(__file__).with_name("logs")
    log_dir.mkdir(exist_ok=True)
    logger = logging.getLogger("structured-logging-exercise")
    logger.handlers.clear()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    for handler in [logging.StreamHandler(sys.stdout), logging.FileHandler(log_dir / "exercise.log")]:
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


def run() -> None:
    logger = configure_logger()
    payload = {"service": "billing", "request_id": "req-204", "event": "invoice-generated"}
    logger.info(json.dumps(payload, sort_keys=True))
    print("Next practice: add loguru sinks, JSON serialization, and severity-based files.")


if __name__ == "__main__":
    run()
