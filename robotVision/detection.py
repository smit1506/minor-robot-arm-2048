#template matching attempt

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('test.jpg')
img_gray = img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template_empty.png',0)
template2 = cv2.imread('template_2.png',0)
w, h = template2.shape[::-1]


value = 0

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 1
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    value += 1
    print(value)

value = 0

res = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
threshold = 0.97
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
    value += 1
    print(value)

cv2.imwrite('res.png',img_rgb)
cv2.imwrite('t2.png',template2)
cv2.imwrite('imgGray.png',img_gray)


