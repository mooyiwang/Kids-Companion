#!/usr/bin/python3.5.3
import os
import test2
from aip import AipSpeech

def record():
    print('recording start')
    os.system('sudo arecord -D "plughw:1,0" -d 5 /home/pi/0Test/test6')
 
def shift():
    print('shift begin')
    os.system('sudo ffmpeg -i /home/pi/0Test/test6  -ac 1 -ar 16000 /home/pi/0Test/test6.wav')
    
def stt():
    result = (test2.speech2text('/home/pi/0Test/test6.wav',1537))
    print("result:",result)
    return result

def VoiceRec():
    if os.path.exists('/home/pi/0Test/test6'):
        os.remove('/home/pi/0Test/test6')
        
    if os.path.exists('/home/pi/0Test/test6.wav'):
        os.remove('/home/pi/0Test/test6.wav')

    record()
    shift()
    i = stt()
    input = i.encode('unicode_escape')
    
    return input
