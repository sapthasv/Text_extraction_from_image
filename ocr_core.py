try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2



def ocr_core(filename):
    
    #Cropped Image
    #import numpy as np
    #source = cv2.imread(filename,1)
    #crop = source[30:1000,30:800]
    #cv2.imshow("Cropped Image",crop)
    
    """
    This function will handle the core OCR processing of images.
    """
    
    pytesseract.pytesseract.tesseract_cmd =  r'C:\Program Files\Tesseract-OCR\tesseract'
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    #Image.open(filename)
    #print(text)
    
    import re
         # Matching the dates in text
    format_1 = re.findall(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{4}",text) # for format  xx-may-xxxx
    format_2 = re.findall(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{1,2}",text) # for format  xx-may-xx
    format_3 = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{4}", text)    # xx-xx-xxxx
    format_4 = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{1,2}", text)    #xx/xx/xx
    format_5 = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{1,2}", text)  #xx-xx-xx
    format_6 = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", text)    #xx/xx/xxxx
    format_7 = re.findall(r"[\d]{1,2}.[\d]{1,2}.[\d]{4}", text)    # xx.xx.xxxx
    format_8 = re.findall(r"[\d]{1}/[\d]{1,2}/[\d]{1,2}", text)    #x/xx/xx
    format_9 = re.findall(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{1,2}",text) # for format  xx-may-xx
    format_10 = re.findall(r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}",text) # xx full month name xxxx
    format_11 = re.findall(r"[\d]{1,2}/[ADFJMNOS]\w*/[\d]{4}",text) # for format  xx/may/xxxx
    format_12 = re.findall(r"[\d]{1}/[\d]{1,2}/[\d]{1,2}", text)    #x/xx/xx
    format_13 = re.findall(r"[\d]{4}-[\d]{1,2}-[\d]{1,2}", text)    # xxxx-xx-xx
    format_14 = re.findall(r"[ADFJMNOS]\w* [\d]{1,2}, [\d]{4}", text) # for format  may xx, xxxx
    
   
    
    for dates_1 in format_1:
        return dates_1
    for dates_2 in format_2:
        return dates_2
    for dates_3 in format_3:
        return dates_3
    for dates_4 in format_4:
        return dates_4
    for dates_5 in format_5:
        return dates_5
    for dates_6 in format_6:
        return dates_6
    for dates_7 in format_7:
        return dates_7
    for dates_8 in format_8:
        return dates_8
    for dates_9 in format_9:
        return dates_9
    for dates_10 in format_10:
        return dates_10
    for dates_11 in format_11:
        return dates_11
    for dates_12 in format_12:
        return dates_12
    for dates_13 in format_13:
        return dates_13
    for dates_14 in format_14:
        return dates_14
        
        
        
    
    
    
#print(ocr_core('4f692e69.jpeg'))

#import os,glob

#os.chdir('All_Images')
#for file in glob.glob('*.jpeg'):
#    print(ocr_core(file))
  #  print(file)
