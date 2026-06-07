import socket


def main() -> None:
    for result in socket.getaddrinfo('localhost', 80, proto=socket.IPPROTO_TCP):
        print(result[4])


if __name__ == '__main__':
    main()
