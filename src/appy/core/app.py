from ..utils import message, img_ascii


def main():
    image_filename = "meirg-logo.jpg"
    output_filename = "meirg-ascii.txt"
    img_ascii.main(image_filename, output_filename)

    name = input("Insert your name: ")
    message.greet(name)


if __name__ == "__main__":
    message.script_path(__file__)
    main()
