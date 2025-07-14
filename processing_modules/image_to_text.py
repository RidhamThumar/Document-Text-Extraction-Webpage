#!/usr/bin/env python
# coding: utf-8


import numpy as np
import cv2
import pytesseract as pytes


import re

from processing_modules.speak import speak_text




# tes_path=r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
# pytes.pytesseract.tesseract_cmd =tes_path

from .query import insert_saved_data,saved_data_fetch
from .databse import db_insert,db_fetch_content
import json

def insert_img_data(text,client_id):
    pdf_data = ''
    data = db_fetch_content(saved_data_fetch %(client_id))
    if len(data)>0:
        if 'img' in list(data[-1][0].keys()):
            data[-1][0]['img'].append(text)
            pdf_data = json.dumps({"img": data})
        else:
           data[-1][0]['img'] = [text]
           pdf_data = json.dumps(data[-1][0])

    else:
        pdf_data = json.dumps({"img": [text]})
    query = insert_saved_data%(pdf_data,client_id)
    db_insert(query)
    return data

def simple_image_extract(image):
    li=[]
    img=cv2.imread(image)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    text=pytes.image_to_string(img, lang='eng')
    if text=='[]'or text==None or text=='':
        h1,w1,=img.shape
        imag=cv2.resize(img,(w1+500,h1+500))
        text=pytes.image_to_string(imag, lang='eng')
        Text_1=text.splitlines()
        for i in Text_1:
            g=re.findall(r'[a-z, A-z, 0-9,/,*]',i)
            li.append(''.join(g))
        for j in li:
            if j=='':
                li.remove(j) 
        speak_text(' '.join(li))   
        return ' '.join(li)
    else:
        h,w=img.shape
        img=cv2.resize(img,(w+100,h+100))
        text_1=text.splitlines()
        for i in text_1:
            g=re.findall(r'[a-z, A-z, 0-9, /, *,-,(,)]',i)
            li.append(''.join(g))
        for j in li:
            if j=='':
                li.remove(j)

        speak_text(' '.join(li))  
        return ' '.join(li)
     
    
    
    
            
            
        
    

