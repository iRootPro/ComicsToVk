import requests
import os
import random

URL_BASE = 'https://xkcd.com/'


def get_last_num_comics():
    url = f'{URL_BASE}info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    num = response.json()['num']
    return num


def get_random_comics_url(num):
    comics_num = random.randint(1, num)
    url = f'{URL_BASE}{comics_num}/info.0.json'

    return url


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


def get_comics_from_xkcd():
    url = get_random_comics_url(get_last_num_comics())
    response = requests.get(url)
    response.raise_for_status()
    image_url = response.json()['img']
    comment_image = response.json()['alt']
    download_image_from_xkcd(image_url)

    return comment_image
