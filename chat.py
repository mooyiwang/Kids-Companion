#!/usr/bin/python
import os
import test2
import turing
import time
import VoiceSyn
from aip import AipSpeech

def record():
    print('recording start')
    os.system('sudo arecord -D "plughw:1,0" -d 5 /home/pi/0Test/test4')
 
def shift():
    print('shift begin')
    os.system('sudo ffmpeg -i /home/pi/0Test/test4  -ac 1 -ar 16000 /home/pi/0Test/test4.wav')
    
def stt():
    result = test2.speech2text('/home/pi/0Test/test4.wav',1537)
    print("result:",result)
    return result

def Chatting():
    os.system(' omxplayer -o local /home/pi/Music/beginchatting.mp3')
    time.sleep(1)
    cnt=0
    while cnt < 5:
        if os.path.exists('/home/pi/0Test/test4'):
            os.remove('/home/pi/0Test/test4')
            
        if os.path.exists('/home/pi/0Test/test4.wav'):
            os.remove('/home/pi/0Test/test4.wav')
            
        if os.path.exists('/home/pi/0Test/audio.mp3'):
            os.remove('/home/pi/0Test/audio.mp3')

        record()
        shift()
        input = stt()
        response = turing.Turing(input)
        
        VoiceSyn.VoiceSyn(response)
        
        os.system(' omxplayer -o local /home/pi/0Test/audio.mp3')
        
        cnt = cnt + 1
    os.system(' omxplayer -o local /home/pi/Music/endchatting.mp3')    