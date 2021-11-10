#!/usr/bin/python
#coding=UTF-8
import requests
import base64
from aip import AipSpeech
base_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
APP_ID = '	23956384'
API_KEY = 'fTahsphF8LwPBeVnK9GppvZ3'
SECRET_KEY = 'ii67ZkI4YlUF6g3iTFHYgNNKD7gOLMoR'
HOST = base_url % (API_KEY, SECRET_KEY)
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def getToken(host):
    res = requests.post(host)
    return res.json()['access_token']

TOKEN = getToken(HOST)

def speech2text(file,dev_pid=1537):
    with open(file, 'rb') as f:
        speech_data = f.read()
    FORMAT = 'wav'
    RATE = '16000'
    CHANNEL = 1
    CUID = '********'
    SPEECH = base64.b64encode(speech_data).decode('utf-8')
    data = {
        'format': FORMAT,
        'rate': RATE,
        'channel': CHANNEL,
        'cuid': CUID,
        'len': len(speech_data),
        'speech': SPEECH,
        'token': TOKEN,
        'dev_pid':dev_pid
    }
    url = 'https://vop.baidu.com/server_api'
    headers = {'Content-Type': 'application/json'}
    print('waiting...')
    r = requests.post(url, json=data, headers=headers)
    Result = r.json()
    if 'result' in Result:
        return Result['result'][0]
    else:
        return "Error!"
    


def change_to_mp3(content='Please input:',turn=1,mp3_name='17k'):
    result  = client.synthesis(content, 'zh', 1, {
        'vol': 5,'per':0
    })
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)

