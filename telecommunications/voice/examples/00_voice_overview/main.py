PHASES = ['REGISTER', 'INVITE', '200 OK', 'ACK', 'RTP media', 'BYE']


def main() -> None:
    for phase in PHASES:
        print(phase)


if __name__ == '__main__':
    main()
