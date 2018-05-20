import requests
import yaml
import json
import os
import base64
import time

from imgurpython import ImgurClient
from requests.exceptions import ConnectionError

IMGUR_CLIENT = ''
IMGUR_SECRET = ''
REFRESH_TOKEN = ''


if __name__ == "__main__":
    client = ImgurClient(IMGUR_CLIENT, IMGUR_SECRET, refresh_token=REFRESH_TOKEN)
    url = 'https://api.imgur.com/3/image/'
    images_directory = './tarot_cards'
    description_directory = './tarot_descriptions'


    for description_filename, image_filename in zip(
                                    sorted(os.listdir(description_directory)),
                                    sorted(os.listdir(images_directory))):
        title = description_filename
        client.auth.refresh()
        print(description_filename)
        print(image_filename)
        print()
        with open(description_directory+'/'+description_filename, 'r') as file:
            description = file.read()

        with open(images_directory+'/'+image_filename, 'rb') as file:
            image = base64.b64encode(file.read())
        payload = {
            'title': title,
            'desription': description,
            'image': image,
            'album': '1CDzADk'
        }
        try:
            a = requests.post(
                url=url.format(id=id),
                headers={'Authorization':'Bearer '+client.auth.get_current_access_token()},
                data=payload
            )
            print(a.text)
            print(a.status_code)
        except ConnectionError:
            time.sleep(5)
