PHASES = ['REGISTER', 'INVITE', '200 OK', 'ACK', 'RTP media', 'BYE']


def signaling_steps() -> list[str]:
    raise NotImplementedError
