import requests
import os
import random

import files

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


def get_comics_from_xkcd():
    url = get_random_comics_url(get_last_num_comics())
    response = requests.get(url)
    response.raise_for_status()
    response_from_server_xkcd = response.json()
    image_url = response_from_server_xkcd['img']
    comment_image = response_from_server_xkcd['alt']
    files.download_image_from_xkcd(image_url)

    return comment_image
