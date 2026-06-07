"""Reference solution for lesson: 09_loguru_structured_logging."""
from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from uuid import uuid4


class BoundLogger:
    def __init__(self, logger: logging.Logger, context: dict[str, object]) -> None:
        self.logger = logger
        self.context = context

    def bind(self, **context: object) -> "BoundLogger":
        return BoundLogger(self.logger, {**self.context, **context})

    def _emit(self, level: str, message: str, **fields: object) -> None:
        payload = {**self.context, **fields, "message": message}
        getattr(self.logger, level)(json.dumps(payload, sort_keys=True))

    def info(self, message: str, **fields: object) -> None:
        self._emit("info", message, **fields)

    def error(self, message: str, **fields: object) -> None:
        self._emit("error", message, **fields)


def configure_logger():
    log_dir = Path(__file__).with_name("logs")
    log_dir.mkdir(exist_ok=True)
    try:
        from loguru import logger

        logger.remove()
        logger.add(sys.stderr, level="DEBUG")
        logger.add(log_dir / "info.log", level="INFO", rotation="25 KB", retention=3)
        logger.add(log_dir / "errors.log", level="ERROR", rotation="25 KB", retention=3)
        logger.add(log_dir / "events.jsonl", level="INFO", serialize=True)
        return logger.bind(service="fulfillment", env="prod")
    except ImportError:
        logger = logging.getLogger("structured-logging-solution")
        logger.handlers.clear()
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        for handler in [
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_dir / "info.log"),
            logging.FileHandler(log_dir / "errors.log"),
        ]:
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        print("loguru not installed; using stdlib structured logging fallback.")
        return BoundLogger(logger, {"service": "fulfillment", "env": "prod"})


def run() -> None:
    logger = configure_logger()
    request_logger = logger.bind(request_id=str(uuid4())[:8], batch_id="batch-77")
    request_logger.info("shipment export started", severity="info")
    request_logger.info("shipment export finished", severity="info", records=128)
    if hasattr(request_logger, "error"):
        request_logger.error("sample error event", severity="error", reason="demonstration")


if __name__ == "__main__":
    run()
