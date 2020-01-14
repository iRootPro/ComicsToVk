from dotenv import load_dotenv
import os

import vk


def main():
    client_id_vk = os.getenv('CLIENT_ID_VK')
    access_token_vk = os.getenv('ACCESS_TOKEN_VK')
    group_id_vk = os.getenv('GROUP_ID_VK')
    print(vk.publish_to_public(access_token_vk, group_id_vk))

if __name__ == '__main__':
    load_dotenv()
    main()

