import Image  
import ImageEnhance  
import ImageFilter  
import sys  
from pytesser import *
import cv2
import numpy as np


img = cv2.imread('Letter_C.jpg')
imblur = cv2.blur(img,(5,5))
imhsv = cv2.cvtColor(imblur,cv2.COLOR_BGR2HSV)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)

#the range of colour
lower_red = np.array([0,21,161]) 
upper_red = np.array([183,210,255])

mask = cv2.inRange(imhsv, lower_red, upper_red)
#res = cv2.bitwise_and(img,img, mask = mask)
ret,thresh = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)

cv2.namedWindow('imred',cv2.WINDOW_NORMAL)
cv2.imshow('imred',thresh)

cv2.imwrite('imred.jpg',thresh)

imtest = Image.open('imred.jpg')
text = image_to_string(imtest)
print 'the letter in the picture is: '
print text

cv2.waitKey(0)
cv2.destroyAllWindows()
