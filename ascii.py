from PIL import Image
import numpy as np

CHARS = '@#S%?*+;:,. '

def scale_image(image, new_width=50):
    width, height = image.size
    ratio = height / 2 / width
    new_height = int(new_width * ratio)
    new_image = image.resize((new_width, new_height))
    return new_image

def grayscale_image(image):
    return image.convert("L")


def map_pixels_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ''

    for pixel in pixels:
        for pixel_value in pixel:
            ascii_str += CHARS[pixel_value // 22]
    return ascii_str


def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)

        image = scale_image(image, new_width)
        image = grayscale_image(image)

        ascii_str = map_pixels_to_ascii(image)

        img_width = image.width
        ascii_str_len = len(ascii_str)
        ascii_img = '\n'.join([ascii_str[i:i + img_width] for i in range(0, ascii_str_len, img_width)])

        return ascii_img
    except Exception as e:
        print(f"Error: {e}")
        return None


ascii_art = convert_image_to_ascii('Thumbnail.png', 180)
if ascii_art:
    print(ascii_art)