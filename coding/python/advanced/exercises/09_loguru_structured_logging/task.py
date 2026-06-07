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


def describe_upgrade_path() -> None:
    print("Upgrade path:")
    print("- replace stdlib setup with loguru.add(...) sinks")
    print("- enable serialize=True for machine-readable logs")
    print("- bind request_id and customer_id per operation")
    print("- split INFO and ERROR logs into separate files")


def log_invoice_event(logger: logging.Logger, invoice_id: str, status: str) -> None:
    payload = {
        "service": "billing",
        "request_id": "req-204",
        "invoice_id": invoice_id,
        "status": status,
    }
    logger.info(json.dumps(payload, sort_keys=True))


def run() -> None:
    logger = configure_logger()
    log_invoice_event(logger, "INV-204", "generated")
    log_invoice_event(logger, "INV-205", "emailed")
    print("exercise log file: logs/exercise.log")
    describe_upgrade_path()


if __name__ == "__main__":
    run()
