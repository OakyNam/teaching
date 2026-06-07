TRAFFIC_CLASSES = ['voice-media', 'voice-signaling', 'api', 'backup']


def main() -> None:
    for item in TRAFFIC_CLASSES:
        print(item)


if __name__ == '__main__':
    main()
