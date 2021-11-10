#!/usr/bin/python
#_*_ coding:UTF-8 _*_
# @author: zdl 

from aip import AipSpeech
import os
import ffmpeg

'''APPID AK SK'''
APP_ID = '23956384'
API_KEY = 'fTahsphF8LwPBeVnK9GppvZ3'
SECRET_KEY = 'ii67ZkI4YlUF6g3iTFHYgNNKD7gOLMoR'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):   #filePath
    with open(filePath, 'rb') as fp:
        return fp.read()

		
def stt(filename):
    ffmpeg.input(filename).output('res.wav', ar=16000).run()
    result = client.asr(get_file_content('res.wav'),
                        'wav',
                        16000,
                        {'dev_pid': 1537,}    
                        )
    print result

    if result['err_msg']=='success.':
        word = result['result'][0].encode('utf-8')       # utf-8
        if word!='':
            if word[len(word)-3:len(word)]=='，':
                print word[0:len(word)-3]
                with open('demo.txt','w') as f:
                    f.write(word[0:len(word)-3])
                f.close()
            else:
                print (word.decode('utf-8').encode('gbk'))
                with open('demo.txt','w') as f:
                    f.write(word)
                f.close()
        else:
            print "Wrong format."
    else:
        print "Error!"

# main
if __name__ == '__main__':
    
    stt('test.wav')
