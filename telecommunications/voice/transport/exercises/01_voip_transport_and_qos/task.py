TRAFFIC_CLASSES = ['voice-media', 'voice-signaling', 'api', 'backup']


def high_priority_classes() -> list[str]:
    raise NotImplementedError
