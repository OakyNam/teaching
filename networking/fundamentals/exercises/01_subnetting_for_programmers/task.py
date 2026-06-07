from ipaddress import ip_network


def usable_host_count(cidr: str) -> int:
    network = ip_network(cidr, strict=True)
    raise NotImplementedError


if __name__ == '__main__':
    print(usable_host_count('10.0.0.64/26'))
