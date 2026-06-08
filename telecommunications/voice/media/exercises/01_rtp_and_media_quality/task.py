METRICS = {
    'latency_ms': 35,
    'jitter_ms': 8,
    'packet_loss_percent': 0.2,
}


def is_good_call(metrics: dict[str, float]) -> bool:
    raise NotImplementedError
