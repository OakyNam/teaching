PHASES = ['REGISTER', 'INVITE', '200 OK', 'ACK', 'RTP media', 'BYE']


def signaling_steps() -> list[str]:
    return PHASES[:4] + PHASES[-1:]
