import cv2
import numpy as np
import imutils

img = cv2.imread("test14.jpg")
img1 = imutils.resize(img)
img2 = img1[197:373, 181:300]

cv2.imshow("frame2",img)
cv2.imshow("frame",img2)
if cv2.waitKey(300000) & ord('a'):
   print "pressed a"
