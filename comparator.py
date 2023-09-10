from io import BytesIO

from PIL import Image
from skimage.metrics import structural_similarity as ssim
from skimage.color import rgb2gray
import numpy as np

from renderer import Renderer


class Comparator:

    @staticmethod
    def _compare_images(image_a: Image, image_b: Image):
        image_a_gray = rgb2gray(np.array(image_a))
        image_b_gray = rgb2gray(np.array(image_b))

        (score, diff) = ssim(image_a_gray, image_b_gray, full=True)

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