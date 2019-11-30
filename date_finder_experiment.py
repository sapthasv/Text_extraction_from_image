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
    #format_10 = re.findall(r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}",text) # xx full month name xxxx
    #format_11 = re.findall(r"[\d]{1,2}/[ADFJMNOS]\w*/[\d]{4}",text) # for format  xx/may/xxxx
    #format_12 = re.findall(r"[\d]{1}/[\d]{1,2}/[\d]{1,2}", text)    #x/xx/xx
    #format_13 = re.findall(r"[\d]{4}-[\d]{1,2}-[\d]{1,2}", text)    # xxxx-xx-xx
    #format_14 = re.findall(r"[ADFJMNOS]\w* [\d]{1,2}, [\d]{4}", text) # for format  may xx, xxxx
    
   
    
    
    if len(format_1) > 0:
        text = format_1
        text1 = text
        print(text1)
        
    elif len(format_2) > 0:
        text = format_2
        text2 = text
        print(text2)
        
    elif len(format_3) > 0:
        text = format_3
        text3 = text
        print(text3)

    elif len(format_4) > 0:
        text = format_4
        text4 = text
        print(text4)
        
    elif len(format_5) > 0:
        text = format_5
        text5 = text
        print(text5)
        
    elif len(format_6) > 0:
        text = format_6
        text6 = text
        print(text6)
        
    elif len(format_7) > 0:
        text = format_7
        text7 = text
        print(text7)
        
    elif len(format_8) > 0:
        text = format_8
        text8 = text
        print(text8)
        
    elif len(format_9) > 0:
        text = format_9
        text9 = text
        print(text9)
        
    # date returned will be a datetime.datetime object. here we are only using the first match.
    else:
        print('No dates found')
    

        
    
    
    
#print(ocr_core('0efaa622.jpeg'))

#import os,glob

#os.chdir('All_Images')
#for file in glob.glob('*.jpeg'):
 #   print(ocr_core(file))
  #  print(file)
