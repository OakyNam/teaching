OIDS = {
    'sysName': '1.3.6.1.2.1.1.5.0',
    'ifInOctets': '1.3.6.1.2.1.2.2.1.10',
    'ifOutOctets': '1.3.6.1.2.1.2.2.1.16',
}


def main() -> None:
    for name, oid in OIDS.items():
        print(f'{name}: {oid}')


if __name__ == '__main__':
    main()
