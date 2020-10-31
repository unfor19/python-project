import os

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to Python Version < 3.7 `importlib_resources`.
    import importlib_resources as pkg_resources  # noqa: 401

from .. import assets  # relative-import the *package* containing the data files # noqa: 501
from PIL import Image


def img_to_ascii(image_absolute_path, output_absolute_path):
    # Source: https://medium.com/@03A_R/generating-ascii-art-from-colored-image-using-python-a044c29176b5 # noqa: 501
    # pass the image as command line argument
    img = Image.open(image_absolute_path)

    # resize the image
    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    # new size of image
    # print(img.size)

    # convert image to greyscale format
    img = img.convert('L')

    pixels = img.getdata()

    # replace each pixel with a character from array
    chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list # noqa: 501
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width]
                   for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    with open(output_absolute_path, 'w') as fs:
        fs.write(ascii_image)


def main(image_filename, output_filename):
    # Get absolute path of image
    with pkg_resources.path(assets, image_filename) as fs:
        image_absolute_path = fs.absolute()

    # Get output file full path
    cwd = os.getcwd()
    output_absolute_path = os.path.join(cwd, output_filename)

    img_to_ascii(image_absolute_path, output_absolute_path)
    print(f"Created the file: {output_absolute_path}")
