import cv2
import numpy as np

img = cv2.imread('test.png',0)

ret, thresh = cv2.threshold(img, 127, 255,0)
im2,contours,hierarchy = cv2.findContours(thresh,2,1)

value = 0
for cnr in range(0,len(contours)):
    cnt = contours[cnr]
    img = cv2.drawContours(img,cnt,-1,(255,0,0),3)
    print(value)
    cv2.imshow('img', img)
    k = cv2.waitKey(0)
    value = value + 1
cv2.destroyAllWindows()
