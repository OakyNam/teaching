METRICS = {
    'latency_ms': 35,
    'jitter_ms': 8,
    'packet_loss_percent': 0.2,
}


def is_good_call(metrics: dict[str, float]) -> bool:
    return metrics['latency_ms'] < 150 and metrics['jitter_ms'] < 30 and metrics['packet_loss_percent'] < 1.0
