import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
header = {
    "Content-type": "application/x-www-form-urlencoded",
    "Authorization": f"Bearer {API_TOKEN}",
}
msg = "TEST MESSAGE FOR KAKAOTALK"
record = {
    "template_object": '{"object_type": "text",  "text":"'
    + msg
    + '",  "link": {"web_url": "http://103.22.220.149:55555", "mobile_web_url": "http://103.22.220.149:55555" },  "button_title": "바로 확인" }'
}
print(record)
res = requests.post(url, data=record, headers=header)
print(res.text)
