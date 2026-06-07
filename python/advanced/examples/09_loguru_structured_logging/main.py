"""Runnable example for lesson: 09_loguru_structured_logging."""
from __future__ import annotations

import json
import logging
import sys
from pathlib import Path
from uuid import uuid4


class BoundStdlibLogger:
    def __init__(self, logger: logging.Logger, context: dict[str, object]) -> None:
        self.logger = logger
        self.context = context

    def bind(self, **context: object) -> "BoundStdlibLogger":
        return BoundStdlibLogger(self.logger, {**self.context, **context})

    def _emit(self, level: str, message: str, **fields: object) -> None:
        payload = {**self.context, **fields, "message": message}
        getattr(self.logger, level)(json.dumps(payload, sort_keys=True))

    def info(self, message: str, **fields: object) -> None:
        self._emit("info", message, **fields)

    def warning(self, message: str, **fields: object) -> None:
        self._emit("warning", message, **fields)

    def exception(self, message: str, **fields: object) -> None:
        self._emit("exception", message, **fields)


def configure_logger():
    log_dir = Path(__file__).with_name("logs")
    log_dir.mkdir(exist_ok=True)
    try:
        from loguru import logger

        logger.remove()
        logger.add(sys.stderr, level="DEBUG")
        logger.add(log_dir / "app.log", level="INFO", rotation="25 KB", retention=3)
        logger.add(log_dir / "app.jsonl", level="INFO", serialize=True)
        return logger.bind(service="checkout", env="dev")
    except ImportError:
        fallback = logging.getLogger("advanced-loguru-example")
        fallback.handlers.clear()
        fallback.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        for handler in [logging.StreamHandler(sys.stdout), logging.FileHandler(log_dir / "app.log")]:
            handler.setFormatter(formatter)
            fallback.addHandler(handler)
        print("loguru not installed; using stdlib logging fallback.")
        return BoundStdlibLogger(fallback, {"service": "checkout", "env": "dev"})


def process_order(logger, order_id: str, *, fail: bool = False) -> None:
    request_logger = logger.bind(request_id=str(uuid4())[:8], order_id=order_id)
    request_logger.info("starting order sync", level_name="INFO")
    try:
        if fail:
            raise ValueError("payment verification failed")
        request_logger.info("order synced", level_name="INFO")
    except Exception:
        request_logger.exception("order sync failed", level_name="ERROR")


def main() -> None:
    logger = configure_logger()
    process_order(logger, "ORD-1001")
    process_order(logger, "ORD-1002", fail=True)


if __name__ == "__main__":
    main()
