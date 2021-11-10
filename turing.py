# coding=UTF-8
#!/usr/bin/python
# 与机器人对话：调用的是图灵机器人
import requests
import json
 
# 图灵机器人的API_KEY、API_URL
turing_api_key = "c75b3fd5c6d745299bfd79aabb680fd9"
api_url = "http://openapi.tuling123.com/openapi/api/v2"  # 图灵机器人api网址
headers = {'Content-Type': 'application/json;charset=UTF-8'}
 
 
# 图灵机器人回复
def Turing(text_words=""):
    req = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": text_words
            },
 
            "selfInfo": {
                "location": {
                    "city": "深圳",
                    "province": "广东",
                    "street": "桃源街道"
                }
            }
        },
        "userInfo": {
            "apiKey": "c75b3fd5c6d745299bfd79aabb680fd9",   # 你的图灵机器人apiKey
            "userId": "Luga"  
        }
    }
 
    req["perception"]["inputText"]["text"] = text_words
    response = requests.request("post", api_url, json=req, headers=headers)
    response_dict = json.loads(response.text)
 
    result = response_dict["results"][0]["values"]["text"]
    print("AI Robot said: " + result)
    return result
