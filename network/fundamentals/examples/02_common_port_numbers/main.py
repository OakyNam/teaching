COMMON_PORTS = {
    22: 'SSH',
    53: 'DNS',
    80: 'HTTP',
    443: 'HTTPS',
    5432: 'PostgreSQL',
    6379: 'Redis',
}


def main() -> None:
    for port, service in sorted(COMMON_PORTS.items()):
        print(f'{port}: {service}')


if __name__ == '__main__':
    main()
