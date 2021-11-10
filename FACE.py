#!/usr/bin/env python3
#coding=UTF-8
from aip import AipFace
#import urllib.request
import base64
import time
from numpy import *
import cv2
import pygame
import os

#百度人脸识别API账号信息
APP_ID = '24099561 '
API_KEY = 'HGUsYT2gU5PWjXME3nFR5QVw'
SECRET_KEY ='Glo5HhHYGiMGztQSIZzhHYrHKQioXDBa'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)#创建一个客户端用以访问百度云
#图像编码方式
IMAGE_TYPE='BASE64'
#用户组
GROUP = 'Luga'
 
#照相函数
def getimage():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640) # set video widht
    cap.set(4, 480) # set video height
    time.sleep(2)   
    ret,frame = cap.read()
    rows, cols, channels = frame.shape
    print(cols, rows, channels)
    ret,frame = cap.read()
    dst = frame
    cv2.imshow('usb camera', dst)
 
    filename = '/home/pi/' +'faceimage.jpg'
    cv2.imwrite(filename, dst)
    print(filename)
    cap.release()
    cv2.destroyAllWindows()
#对图片的格式进行转换
def transimage():
    f = open('/home/pi/faceimage.jpg','rb')
    img = base64.b64encode(f.read())
    img64 = str(img).encode('utf-8')
   #img64 = str(img).encoding('UTF-8')
    return img64
#上传到百度api进行人脸检测
def go_api(image):
    result = client.search(image, IMAGE_TYPE, GROUP);#在百度云人脸库中寻找有没有匹配的人脸
    if result['error_msg'] == 'SUCCESS':#如果成功了
        name = result['result']['user_list'][0]['user_id']#获取名字
        score = result['result']['user_list'][0]['score']#获取相似度
        if score > 80:#如果相似度大于80
            if name == 'Luga':

                print("欢迎")
                time.sleep(3)
            return 1
        else:
            print("对不起，我不认识你！")
            os.system(' omxplayer -o local /home/pi/Music/stranger.mp3')
            #pygame.mixer.init()
            #pygame.mixer.music.load('/home/pi/Music/stranger.mp3')
            #pygame.mixer.music.play()
            return 0
        
        
    if result['error_msg'] == 'pic not has face':
        print('检测不到人脸')
        os.system(' omxplayer -o local /home/pi/Music/noface.mp3')
        time.sleep(2)
        return 2
    else:
        print(str(result['error_code']) +''+str( result['error_code']))
        return 3
#主函数
def FaceRec():  
    flag = 0
    cnt = 0
    while cnt<3:
        print('准备')
        if True:
            getimage()    #拍照
            img = transimage()     #转换照片格式
            res = go_api(img)        #将转换了格式的图片上传到百度云
            if(res == 1):      #是人脸库中的人
                os.system(' omxplayer -o local /home/pi/Music/greet.mp3')
                #pygame.mixer.init()
                #pygame.mixer.music.load('/home/pi/Music/greet.mp3')
                #pygame.mixer.music.play()
                flag = 1
                break
            else:
                cnt+=1
                print('稍等三秒进入下一个')
                time.sleep(3)
    return flag
