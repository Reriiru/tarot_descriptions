import requests
import yaml
import json
import os
import time

from imgurpython import ImgurClient
from requests.exceptions import ConnectionError

IMGUR_CLIENT = ''
IMGUR_SECRET = ''
REFRESH_TOKEN = ''


if __name__ == "__main__":
    client = ImgurClient(IMGUR_CLIENT, IMGUR_SECRET, refresh_token=REFRESH_TOKEN)
    album = sorted(client.get_album_images('TLU5N'), key=lambda x: x.description)
    url = 'https://api.imgur.com/3/image/{id}'
    directory = './tarot_descriptions'
    client.auth.refresh()

    for card, filename in zip(album, sorted(os.listdir(directory))):
        id = card.id
        title = filename
        with open(directory+'/'+filename, 'r') as file:
            description = file.read()
        payload = {
            'title': title,
            'desription': description
        }
        try:
            requests.post(
                url=url.format(id=id),
                headers={'Authorization':'Bearer '+client.auth.get_current_access_token()},
                data=payload
            )
        except ConnectionError:
            time.sleep(5)
