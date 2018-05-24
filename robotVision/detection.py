#template matching attempt

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('test9.jpg')
img_gray = img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('templates/template_2_big.png',0)
template2 = cv2.imread('templates/template_4_big.png',0)
template3 = cv2.imread('templates/template_field.png',0)


def getMatches(template,color):
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    last_pts = []

    for pt in zip(*loc[::-1]):
        is_invalid_match = False
        for last_pt in last_pts:
            if (last_pt) and abs(pt[0] - last_pt[0]) <= 10 and abs(pt[1] - last_pt[1]) <= 10:
                is_invalid_match = True
        if is_invalid_match:
            continue
        print(pt)
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), color , 2)
        last_pts.append(pt)


getMatches(template,(0,255,0))
getMatches(template2,(255,0,0))
getMatches(template3,(0,0,255))


cv2.imwrite('res.png',img_rgb)
