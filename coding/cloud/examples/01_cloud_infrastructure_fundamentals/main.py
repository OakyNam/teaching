LAYERS = {
    'identity': ['roles', 'service accounts', 'least privilege'],
    'networking': ['subnets', 'routing', 'dns', 'security groups'],
    'compute': ['virtual machines', 'containers', 'serverless'],
    'data': ['object storage', 'managed sql', 'caches'],
}


def main() -> None:
    for layer, topics in LAYERS.items():
        print(f'{layer}: {", ".join(topics)}')


if __name__ == '__main__':
    main()
