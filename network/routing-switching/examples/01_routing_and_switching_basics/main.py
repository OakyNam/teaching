from ipaddress import ip_address, ip_network


ROUTES = {
    ip_network('10.0.0.0/24'): 'local-switch',
    ip_network('0.0.0.0/0'): 'default-gateway',
}


def next_hop(destination: str) -> str:
    address = ip_address(destination)
    matching = [route for route in ROUTES if address in route]
    return ROUTES[max(matching, key=lambda route: route.prefixlen)]


def main() -> None:
    print(next_hop('10.0.0.25'))
    print(next_hop('8.8.8.8'))


if __name__ == '__main__':
    main()
