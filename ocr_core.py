# importing libraries 

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    
    #Cropped Image
    #import numpy as np
    #source = cv2.imread(filename,1)
    #crop = source[30:1000,30:800]
    #cv2.imshow("Cropped Image",crop)
    
  
    '''

    # Improting Image class from PIL module 
    from PIL import Image 
      
    # Opens a image in RGB mode 
    im = Image.open(filename) 
    im.size
    # Setting the points for cropped image 
    left = 10
    top = 100
    right = 650
    bottom = 800
      
    # Cropped image of above dimension 
    # (It will not change orginal image) 
    im1 = im.crop((left, top, right, bottom)) 
      
    # Shows the image in image viewer 
    im1.show() 
    
    '''
    

    """
    This function will handle the core OCR processing of images.
    """
    # extracting the text from image
    
    pytesseract.pytesseract.tesseract_cmd =  r'C:\Program Files\Tesseract-OCR\tesseract'
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    #Image.open(filename)
    print(text)
    
    import re


    
    # reading all the formats
    format_1 = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", text)    #xx/xx/xxxx
    format_2 = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{1,2}", text)    #xx/xx/xx
    format_3 = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{4}", text)    # xx-xx-xxxx
    format_4 = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{1,2}", text)  #xx-xx-xx
    format_5 = re.findall(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{4}",text) # for format  xx-may-xxxx
    format_6 = re.findall(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{1,2}",text) # for format  xx-may-xx
    format_7 = re.findall(r"[\d]{1,2}/[ADFJMNOS]\w*/[\d]{4}",text) # for format  xx/may/xxxx
    format_8 = re.findall(r"[\d]{1,2}/[ADFJMNOS]\w*/[\d]{1,2}",text) # for format  xx/may/xx
    format_9 = re.findall(r"[\d]{1,2}.[\d]{1,2}.[\d]{4}", text)    # xx.xx.xxxx
    format_10 = re.findall(r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}",text) # xx full month name xxxx
    format_11 = re.findall(r"[\d]{1}/[\d]{1,2}/[\d]{1,2}", text)    #x/xx/xx
    format_12 = re.findall(r"[\d]{4}-[\d]{1,2}-[\d]{1,2}", text)    # xxxx-xx-xx
    format_13 = re.findall(r"[ADFJMNOS]\w* [\d]{1,2}, [\d]{4}", text) # for format  may xx, xxxx
    
    
    
    # comparing all above formats on the text
    if len(format_1) > 0:
        text = format_1
        return text

    elif len(format_2) > 0:
        text = format_2
        return text
    
    elif len(format_3) > 0:
        text = format_3
        return text
    
    elif len(format_4) > 0:
        text = format_4
        return text
    
    elif len(format_5) > 0:
        text = format_5
        return text
    
    elif len(format_6) > 0:
        text = format_6
        return text
    
    elif len(format_7) > 0:
        text = format_7
        return text
    
    elif len(format_8) > 0:
        text = format_8
        return text
    
    elif len(format_9) > 0:
        text = format_9
        return text
    
    elif len(format_10) > 0:
        text = format_10
        return text
    
    elif len(format_11) > 0:
        text = format_11
        return text

    elif len(format_12) > 0:
        text = format_12
        return text
    
    elif len(format_13) > 0:
        text = format_13
        return text

    # date returned will be a datetime.datetime object. here we are only using the first match.
    else:
        print('No dates found')
    

    
   

#print(ocr_core('0daa6a1c.jpeg'))    
    


#import os,glob

#os.chdir('All_Images')
#for file in glob.glob('*.jpeg'):
 #   print(ocr_core(file))
  #  print(file)

