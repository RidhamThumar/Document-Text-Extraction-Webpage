from pyzbar.pyzbar import decode
import cv2 #COMPUTER VISION LIBRARY


from .query import insert_saved_data,saved_data_fetch
from .databse import db_insert,db_fetch_content
import json

def insert_qr_data(text,client_id):
    pdf_data = ''
    data = db_fetch_content(saved_data_fetch %(client_id))
    if len(data)>0:
        if 'QR' in list(data[-1][0].keys()):
            data[-1][0]['QR'].append(text)
            pdf_data = json.dumps({"QR": data})
        else:
           data[-1][0]['QR'] = [text]
           pdf_data = json.dumps(data[-1][0])

    else:
        pdf_data = json.dumps({"QR": [text]})
    query = insert_saved_data%(pdf_data,client_id)
    db_insert(query)
    return data


def Decode(image):
      result=[]
      img=cv2.imread(image) # IS LINE KA MATLAB BATA
      
      qdata=decode(img) # USED FOR EXTRACTION OF TEXT
      
      
##      for i in qdata:
##            result.append(i.data.decode('utf-8'))
      res=[i.data.decode('utf-8') for i in qdata] # LIST COMPREHENSION
      return ''.join(res)   #list to string joining   
