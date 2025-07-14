from processing_modules.pdfextract import insert_pdf_data
from processing_modules.image_to_text import insert_img_data
from processing_modules.databse import db_fetch_content
text = ''' test extracted insert_pdf_data'''
# t=insert_pdf_data(text,client_id='User123')
t1=insert_img_data(text,client_id='User123')

print(t1)