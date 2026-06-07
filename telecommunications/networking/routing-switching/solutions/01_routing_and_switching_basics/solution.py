from ipaddress import ip_address


def next_hop(destination: str, routes: dict) -> str:
    address = ip_address(destination)
    matching = [route for route in routes if address in route]
    return routes[max(matching, key=lambda route: route.prefixlen)]
