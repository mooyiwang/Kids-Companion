#coding=UTF-8
#!/usr/bin/python
import difflib
 
 
def string_similar(s1, s2):
	return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


def FuncChoose(Input = ""):
    Func = 4
    similarity = 0
    s1 = string_similar(Input,'\u5531\u513f\u6b4c\ua\ua')
    similarity = s1
    s2 = string_similar(Input,'\u8bb2\u6545\u4e8b\ua')
    if s2 > similarity:
        similarity = s2
    s3 = string_similar(Input,'\u804a\u4f1a\u513f\u5929\ua')
    if s3 > similarity:
        similarity = s3
    s4 = string_similar(Input,'\u518d\u89c1\ua\ua')
    if s4 > similarity:
        similarity = s4
    if similarity < 0.3:
        Func = 5
        similarity = -1
        
    if similarity == s1:
        Func = 1
    elif similarity == s2:
        Func = 2
    elif similarity == s3:
        Func = 3
    elif similarity == s4:
        Func = 4
    
    
    return Func
