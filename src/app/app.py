from ..utils import message


def main():
    name = input("Insert your name: ")
    message.greet(name)


if __name__ == "__main__":
    message.script_path(__file__)
    main()
