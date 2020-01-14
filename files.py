import os
import requests


def get_image_extension(image_url):
    extension = os.path.splitext(image_url)[1]
    return extension


def download_image_from_xkcd(image_url):
    extension_image = get_image_extension(image_url)
    filename = f'comics{extension_image}'

    response = requests.get(image_url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


