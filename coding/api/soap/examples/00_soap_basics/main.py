from xml.etree.ElementTree import Element, SubElement, tostring


def build_envelope(customer_id: str) -> str:
    envelope = Element('soap:Envelope', {'xmlns:soap': 'http://schemas.xmlsoap.org/soap/envelope/'})
    body = SubElement(envelope, 'soap:Body')
    lookup = SubElement(body, 'GetCustomerRequest')
    SubElement(lookup, 'CustomerId').text = customer_id
    return tostring(envelope, encoding='unicode')


def main() -> None:
    print(build_envelope('42'))


if __name__ == '__main__':
    main()
