LAYERS = {
    'identity': ['roles', 'service accounts', 'least privilege'],
    'networking': ['subnets', 'routing', 'dns', 'security groups'],
    'compute': ['virtual machines', 'containers', 'serverless'],
    'data': ['object storage', 'managed sql', 'caches'],
}


def has_layer(name: str) -> bool:
    raise NotImplementedError
