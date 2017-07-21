import json
import requests
import base64

from config import botconfig
from base64 import b64encode
from io import BytesIO
from PIL import Image

def upload_imgur(image, res):
    if res != "default":
        imgrequest = requests.get(image.file_path)
        img = BytesIO(imgrequest.content)
        image2 = Image.open(img)
        im2 = image2.resize((int(res.split('x')[0]), int(res.split('x')[1])), Image.ANTIALIAS)
        temp = BytesIO()
        im2.save(temp, 'png')
        temp.seek(0)

    client_id = botconfig.clientid_imgur
    headers = {"Authorization": "Client-ID " + client_id}
    api_key = botconfig.api_imgur
    url = "https://api.imgur.com/3/upload.json"
    rpost = requests.post(
        url, 
        headers = headers,
        data = {
            'key': api_key, 
            'image': b64encode(temp.read()) if res != "default" else image.file_path, 
            'type': 'base64' if res != "default" else 'url',
            'name': image.file_id,
            'title': image.file_id + 'Upload by @imgurplusbot'
        }
    )
    return json.loads(rpost.text)["data"]["link"] if rpost.status_code == 200 else "Error uploading image."