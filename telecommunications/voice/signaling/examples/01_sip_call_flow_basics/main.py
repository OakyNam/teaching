MESSAGES = ['REGISTER', 'INVITE', '180 Ringing', '200 OK', 'ACK', 'BYE']


def main() -> None:
    for message in MESSAGES:
        print(message)


if __name__ == '__main__':
    main()
