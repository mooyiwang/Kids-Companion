from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '24528871'
API_KEY = '5ScePxaCsc13KdheBxTyxGI0'
SECRET_KEY = 'M9Ub8yLRnIDBvAN3qeSeF8ct2XSvXmcu'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('hello', 'zh', 1, {
    'vol': 10,'spd':6,'pit':5,'per':4
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
    f.close()
print("tts successful")
