from ipaddress import ip_network


def describe_subnet(cidr: str) -> dict[str, str | int]:
    network = ip_network(cidr, strict=True)
    hosts = list(network.hosts())
    return {
        'network': str(network.network_address),
        'broadcast': str(network.broadcast_address),
        'usable_hosts': max(network.num_addresses - 2, 0),
        'first_host': str(hosts[0]) if hosts else 'n/a',
        'last_host': str(hosts[-1]) if hosts else 'n/a',
    }


def main() -> None:
    print(describe_subnet('10.0.0.64/26'))


if __name__ == '__main__':
    main()
