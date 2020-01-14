import requests

import xkcd


URL_BASE = 'https://api.vk.com/method/'


def get_url_for_upload_comics(token, group_id):
    url = f'{URL_BASE}photos.getWallUploadServer'
    params_url = {
        'access_token': token,
        'v': '5.103',
        'group_id': group_id
    }

    response = requests.get(url, params=params_url)
    response.raise_for_status()
    data_from_response = response.json()['response']
    upload_url = data_from_response['upload_url']
    album_id = data_from_response['album_id']
    user_id = data_from_response['user_id']

    return upload_url


def check_error_upload(response_from_sever_vk):
    try:
        return response_from_sever_vk['photo']
    except:
        raise HTTPError


def upload_image_to_server_vk(upload_url, token, group_id):
    payload = {
        'access_token': token,
        'v': '5.103',
        'group_id': group_id
    }

    with open('comics.png', 'rb') as file:
        photo = {
            'photo': file
        }
        response = requests.post(upload_url, files=photo, json=payload)
        response.raise_for_status()

        response_from_sever_vk = response.json()

        check_error_upload(response_from_sever_vk)

        server_vk = response_from_sever_vk['server']
        photo_vk = response_from_sever_vk['photo']
        hash_vk = response_from_sever_vk['hash']
        return server_vk, photo_vk, hash_vk, token


def save_image_to_wall_vk(server_vk, photo_vk, hash_vk, token, group_id):
    url = f'{URL_BASE}photos.saveWallPhoto'
    payload = {
        'access_token': token,
        'v': '5.103',
        'group_id': group_id,
        'server': server_vk,
        'photo': photo_vk,
        'hash': hash_vk
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    response_from_sever_vk = response.json()['response']
    photo_id = response_from_sever_vk[0]['id']
    owner_id = response_from_sever_vk[0]['owner_id']
    return photo_id, owner_id


def post_wall(photo_id, owner_id, message, token, group_id):
    url = f'{URL_BASE}wall.post'
    attachment = f'photo{owner_id}_{photo_id}'
    payload = {
        'access_token': token,
        'v': '5.103',
        'owner_id': -(int(group_id)),
        'attachments': attachment,
        'from_group': 1,
        'message': message
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()['response']


def posting_to_public(token, group_id):
    message = xkcd.get_comics_from_xkcd()
    upload_url = get_url_for_upload_comics(token, group_id)
    server_vk, photo_vk, hash_vk, token = upload_image_to_server_vk(
        upload_url, token, group_id)
    photo_id, owner_id = save_image_to_wall_vk(
        server_vk, photo_vk, hash_vk, token, group_id)
    posted = post_wall(photo_id, owner_id, message, token, group_id)
    if posted['post_id']:
        return 'Ваш комикс опубликован'
    else:
        return 'Ваш комикс не опубликован'
