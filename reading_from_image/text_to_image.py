# This creates image data set to reading from image

import cv2
from data_set import text 
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
cordinateX = 0
cordinateY = 150
color = (255, 0, 0)
fontScale = 0.65
thickness = 1
count = 0
path = '\images'
for x in text:
    word = x.split(",")
    img = np.zeros((1500, 2500), dtype=np.uint8)
    image = img
    for element in word:
        image = cv2.putText(image, element, (cordinateX,cordinateY), font, fontScale, color, thickness)
        cordinateY += 50
        #cv2.imshow('image',image)
    cordinateY = 150
    cv2.imwrite(path+'/image_'+str(count)+'.jpg',image)
    count += 1
cv2.waitKey(0)
