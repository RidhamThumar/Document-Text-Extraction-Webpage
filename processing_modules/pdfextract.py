

import PyPDF2 as pdf
from PyPDF2 import PdfReader,PdfFileReader
import cv2
import os
import pprint
import json
import re # REGULAR EXPRESSION


from .query import insert_saved_data,saved_data_fetch
from .databse import db_insert,db_fetch_content
import json

def insert_pdf_data(text,client_id):
    pdf_data = ''
    data = db_fetch_content(saved_data_fetch %(client_id))
    
    if len(data)>0:
        if 'pdf' in list(data[-1][0].keys()):
            data[-1][0]['pdf'].append(text)
            pdf_data = json.dumps({"pdf": data})
        else:
           data[-1][0]['pdf'] = [text]
           pdf_data = json.dumps(data[-1][0])

    else:
        pdf_data = json.dumps({"pdf": [text]})
    query = insert_saved_data%(pdf_data,client_id)
    db_insert(query)
    return data





def pdftext(filepath,pno):
    if filepath.endswith('.pdf'):
        reader = PdfReader(filepath)
        numOfPages = len(reader.pages)
        #print('inder',(pno!= 0) , (int(pno) in list(range(1,numOfPages+1))))
        if (pno!= 0) and (pno in list(range(1,numOfPages+1))):
            page = reader.pages[pno-1]
            return page.extract_text()
        else:
            return f'{pno} no page is not avilable'
        
