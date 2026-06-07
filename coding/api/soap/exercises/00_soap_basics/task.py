from xml.etree.ElementTree import Element, SubElement, tostring


def build_envelope(customer_id: str) -> str:
    """Return a SOAP envelope string for GetCustomerRequest."""
    raise NotImplementedError


if __name__ == '__main__':
    print(build_envelope('42'))
