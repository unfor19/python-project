from src.app import app
from src.utils import message


def main():
    app.main()


if __name__ == "__main__":
    message.script_path(__file__)
    main()
