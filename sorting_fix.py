import requests
import json
import time

from imgurpython import ImgurClient
from requests.exceptions import ConnectionError

IMGUR_CLIENT = ''
IMGUR_SECRET = ''
REFRESH_TOKEN = ''

if __name__ == "__main__":
    client = ImgurClient(IMGUR_CLIENT, IMGUR_SECRET, refresh_token=REFRESH_TOKEN)
    album = client.get_album_images('TLU5N')
    url = 'https://api.imgur.com/3/image/{id}'
    client.auth.refresh()

    for card in album:
        title = card.description.split('\n')[0]
        print(title, card.title)
        id = card.id
        
        payload = {
            'title': title,
        }

        print(url.format(id=id))
        try:
            a = requests.post(
                url=url.format(id=id),
                headers={'Authorization':'Bearer '+client.auth.get_current_access_token()},
                data=payload
            )
            print(a, a.text)
        except ConnectionError:
            time.sleep(5)
        print(card.title)