import json
import requests
import base64
import imageio
import os, sys

from config import botconfig
from base64 import b64encode
from io import BytesIO
from PIL import Image

def upload_imgur(image):
    try:
        if image.file_path[::-1].split('.')[0][::-1] == "mp4":
            mp4request = requests.get(image.file_path)
            mp4 = BytesIO(mp4request.content)
            gif = imageio.get_reader(mp4,  'ffmpeg')
            fps = gif.get_meta_data()['fps']
            frames = []
            for i,im in enumerate(gif):
                frames.append(im)
            temp = BytesIO()
            imageio.mimsave(temp, frames, format='GIF', fps=fps)
            temp.seek(0)
        elif image.file_path[::-1].split('.')[0][::-1] == "webp":
            imgrequest = requests.get(image.file_path)
            img = BytesIO(imgrequest.content)
            image2 = Image.open(img)
            temp = BytesIO()
            image2.save(temp, 'png')
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
                'image': b64encode(temp.read()) if image.file_path[::-1].split('.')[0][::-1] == "mp4" or image.file_path[::-1].split('.')[0][::-1] == "webp" else image.file_path, 
                'type': 'base64' if image.file_path[::-1].split('.')[0][::-1] == "mp4" or image.file_path[::-1].split('.')[0][::-1] == "webp" else 'url',
                'name': image.file_id,
                'title': image.file_id + 'Upload by @imgurplusbot'
            }
        )
        return json.loads(rpost.text)["data"]["link"] if rpost.status_code == 200 else "Error uploading image."
    except:
        return "Error uploading image."