import os,sys

class xml_string:
    list={}
    list['&']='&amp;'
    list['<']='&lt;'
    list['>']='&gt;'
    def __init__(self):
        pass
        
    def encode(self,text):
        newtext=''
        for l in range(0,len(text)):
            newtext+=self.list.get(text[l],text[l])
        return newtext
