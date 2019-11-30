

# PyTesseract - Simple Python Optical Character Recognition




### Prerequisites

Kindly ensure you have the following installed on your machine:

 Python 3 and above
 Tesseract
 Regexp
 OpenCV
 Datefinder
 An IDE or Editor of your choice

#Simple ocr model for text extraction from the image file.

In this project 
I am using Pytesseract model for text extarction from image and this extracted file from the image is passed into
the regular expression(for pre defined format)

extracted text is comapred with the regular expression date formats.if its matching to particular date for format
and it will be printed

This is passed to front end using simple html file and flask framework and this is deployed in ubuntu server on AWS.

# My observations
This can can able to predict most date file formats , And some times it fails to predict because of blur images,dark images and handwritten images.
# Image quality improvement
I tried to improve images by converting to black and white(using open cv),giving sharpness to image ,parsing particular portion of  cropped image

By doing this kind of image tuning acuracy got increased 6 to 8% , Now accuracy level is about 55 to 58%

# future changes can be made 
still Accuracy can be increased by using deeplearning models on ocr recognition 
To this require lot of images to train the model to get better accuracy 
This will learn the pattern and gives better accuracy by training image again and agian.So this will best approach to get better acuracy 
