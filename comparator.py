import cv2
import numpy as np
from skimage.metrics import structural_similarity
from PIL import Image, ImageDraw, ImageFont

from utils import OperatingSystem, Utils


class Comparator:

    @staticmethod
    def _compare_images(image_a: Image, image_b: Image):
        image_a_gray = cv2.cvtColor(np.array(image_a), cv2.COLOR_RGB2GRAY)
        image_b_gray = cv2.cvtColor(np.array(image_b), cv2.COLOR_RGB2GRAY)

        (score, diff) = structural_similarity(image_a_gray, image_b_gray, full=True)

        return score

    @staticmethod
    def _generate_image(text: str, operating_system: OperatingSystem) -> Image:
        image = Image.new('RGB', (200, 60), color=(73, 109, 137))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(str(Utils.get_font_path(operating_system)), 15)
        draw.text((10, 10), text, font=font, fill=(255, 255, 0))
        image.show()

        return image

    @staticmethod
    def compare_domain_names(domain_name_a: str, domain_name_b: str, operating_system: OperatingSystem) -> float:
        domain_name_a_image = Comparator._generate_image(domain_name_a, operating_system)
        domain_name_b_image = Comparator._generate_image(domain_name_b, operating_system)
        return Comparator._compare_images(domain_name_a_image, domain_name_b_image)
