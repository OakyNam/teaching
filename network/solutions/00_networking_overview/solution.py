STEPS = [
    'Resolve DNS for api.example.com',
    'Open TCP connection to 203.0.113.10:443',
    'Negotiate TLS',
    'Send HTTP request',
    'Receive HTTP response',
]


def main() -> None:
    for index, step in enumerate(STEPS, start=1):
        print(f'{index}. {step}')


if __name__ == '__main__':
    main()
