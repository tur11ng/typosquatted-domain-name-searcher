from io import BytesIO

import cv2
import numpy as np
from skimage.metrics import structural_similarity
from PIL import Image, ImageDraw, ImageFont

from renderer import Renderer


class Comparator:

    @staticmethod
    def _compare_images(image_a: Image, image_b: Image):
        image_a_gray = cv2.cvtColor(np.array(image_a), cv2.COLOR_RGB2GRAY)
        image_b_gray = cv2.cvtColor(np.array(image_b), cv2.COLOR_RGB2GRAY)

        (score, diff) = structural_similarity(image_a_gray, image_b_gray, full=True)

        return score

    @staticmethod
    async def _generate_image(text: str) -> Image:
        image_bytes = await Renderer.render_text(text)
        image = Image.open(BytesIO(image_bytes))
        return image

    @staticmethod
    async def compare_domain_names(domain_name_a: str, domain_name_b: str) -> float:
        domain_name_a_image = await Comparator._generate_image(domain_name_a)
        domain_name_b_image = await Comparator._generate_image(domain_name_b)
        return Comparator._compare_images(domain_name_a_image, domain_name_b_image)
