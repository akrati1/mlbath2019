# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:20:03 2019

@author: dell
"""
try :
     from PIL import Image
except ImportError:
     import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import PyPDF2
from pdf2image import convert_from_path
def ocr_code(inp_img):
    text=pytesseract.image_to_string(inp_img)
    return text
def save_images(pages):
    #This method helps in converting the images in PIL Image file format to the required image format
     index = 1
     for images in pages:
        images.save("F:\\python\\aemigiance_training\\ocr_recognizaation_project\\image\\page_" + str(index) + ".jpg")
        input_data1=Image.open("F:\\python\\aemigiance_training\\ocr_recognizaation_project\\image\\page_" + str(index) + ".jpg")
        text_data1=ocr_code(input_data1)
        text_file=open('F:\\img2txt.txt','w+')
        text_file.write(text_data1)
        text_file.close()
        print(text_data1)  
        index += 1      
file_name='F:\\python\\aemigiance_training\\ocr_recognizaation_project\\Akrati_Sharma_Hired_Certificate.pdf'
img_type=file_name.split('.')[-1]
if img_type=='pdf':
     pages=convert_from_path('F:\\python\\aemigiance_training\\ocr_recognizaation_project\\uppsc_computeroperator.pdf',
     fmt='jpg',thread_count=1,dpi=200)
     save_images(pages)
    
    
else:     
     input_data=Image.open(file_name)
     text_data=ocr_code(input_data)
     text_file=open('img2txt.txt','w+')
     text_file.write(text_data)
     text_file.close()
     print(text_data)

    