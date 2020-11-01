from unittest import TestCase
import src.appy.utils.img_ascii as img_ascii
from os import path, remove


class ApiTestCase(TestCase):

    def test_img_to_ascii(self):
        image_filename = "meirg-logo.jpg"
        output_filename = ".meirg-ascii-test.txt"
        img_ascii.main(image_filename, output_filename)
        output_exists = path.isfile(output_filename)
        remove(output_filename)
        output_deleted = not path.isfile(output_filename)
        self.assertTrue(output_exists and output_deleted)
