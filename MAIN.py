#!/usr/bin/python
#coding= UTF-8
import os
import FACE
import VoiceRec
import pygame
import chat
import test2
import VoiceSyn
import StrSimilar
import time
from aip import AipSpeech

time.sleep(10)

#main function
if __name__ == '__main__':
    FaceRecogResult = FACE.FaceRec()
    if(FaceRecogResult == 1):
        #time.sleep(2)
        os.system(' omxplayer -o local /home/pi/Music/choice.mp3')
        VoiceRecogResult = VoiceRec.VoiceRec()
        Func = StrSimilar.FuncChoose(VoiceRecogResult)
        while Func != 4:
            if Func == 1:
                os.system(' omxplayer -o local /boot/share/MP3/song.mp3')
            elif Func == 2:
                os.system(' omxplayer -o local /boot/share/MP3/story.mp3')
            elif Func == 3:
                chat.Chatting()
            elif Func == 5:
                os.system(' omxplayer -o local /boot/share/MP3/sorry.mp3')
            
            
            #time.sleep(2)
            os.system(' omxplayer -o local /home/pi/Music/continue.mp3')
            VoiceRecogResult = VoiceRec.VoiceRec()
            Func = StrSimilar.FuncChoose(VoiceRecogResult)
        
        os.system(' omxplayer -o local /home/pi/Music/exit.mp3')    
            
    else:
        os.system(' omxplayer -o local /home/pi/Music/exit.mp3')
        
 
    #os.system('sudo shutdown now -h')
        
            
            
    