COMMON_PORTS = {
    22: 'SSH',
    53: 'DNS',
    80: 'HTTP',
    443: 'HTTPS',
    5432: 'PostgreSQL',
    6379: 'Redis',
}


def service_for_port(port: int) -> str:
    raise NotImplementedError
