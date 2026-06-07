from ipaddress import ip_network


def usable_host_count(cidr: str) -> int:
    network = ip_network(cidr, strict=True)
    return max(network.num_addresses - 2, 0)


if __name__ == '__main__':
    print(usable_host_count('10.0.0.64/26'))
