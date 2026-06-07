import socket


def resolve(hostname: str) -> list[str]:
    results = socket.getaddrinfo(hostname, 80, proto=socket.IPPROTO_TCP)
    return sorted({item[4][0] for item in results})
