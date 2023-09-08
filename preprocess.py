import io
import json

import cv2
import numpy as np
from skimage.metrics import structural_similarity
from PIL import Image, ImageDraw, ImageFont
import homoglyphs as hg
import tqdm


def compare_images(image_a: Image, image_b: Image):
    image_a = cv2.cvtColor(np.array(image_a), cv2.COLOR_RGB2BGR)
    image_b = cv2.cvtColor(np.array(image_b), cv2.COLOR_RGB2BGR)

    grayA = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

    (score, diff) = structural_similarity(grayA, grayB, full=True)

    return score


def generate_image(text: str, font_path: str) -> Image:
    image = Image.new('RGB', (200, 60), color=(73, 109, 137))
    d1 = ImageDraw.Draw(image)
    fnt = ImageFont.truetype(font_path, 15)
    d1.text((10, 10), text, font=fnt, fill=(255, 255, 0))

    return image


def get_font_path(os_type):
    if os_type == 'ios':
        return "./assets/sf-pro/SF-Pro-Text-Regular.ttf"
    elif os_type == 'android':
        return "./assets/roboto/Roboto-Regular.ttf"
    elif os_type == 'windows':
        return "./assets/segoe-ui/Segoe-UI.ttf"
    else:
        raise ValueError(f"Unsupported OS type: {os_type}")


def compare_homoglyphs(os_type):
    compared_scores = {}
    font_path = get_font_path(os_type)

    hg_instance = hg.Homoglyphs(languages={'en'}, strategy='load')
    hg_instance.

    hg.Homoglyphs.
    all_chars = []
    for category in categories:
        all_chars.append(chr(next(iter(hg.CATEGORIES[category]))))

    for char in tqdm(all_chars):
        homoglyphs = hg_instance.get_homoglyphs(char)
        if homoglyphs:
            char_image = generate_image(char, font_path)
            for homoglyph in homoglyphs:
                if char != homoglyph:
                    homoglyph_image = generate_image(homoglyph, font_path)
                    similarity_index = compare_images(char_image, homoglyph_image)
                    compared_scores[f'{char} vs {homoglyph}'] = similarity_index

    with open('compared_scores.json', 'w') as f:
        json.dump(compared_scores,f,indent=4)