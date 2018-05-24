#template matching attempt

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('test9.jpg')
img_gray = img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('templates/template_2_big.png',0)
template2 = cv2.imread('templates/template_4_big.png',0)
template3 = cv2.imread('templates/template_field.png',0)
template4 = cv2.imread('templates/template_8_big.png',0)
template5 = cv2.imread('templates/template_16_big.png',0)

grid = []
board = [0] * 16





def getMatches(template,color, value):
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

        index = 0
        dim = ((pt[0],pt[1]), (pt[0]+w,pt[1]+h))
        
        for point in grid:
            if (point[0][0] < dim[0][0]) and (point[0][1] < dim[0][1]) and (point[1][0] > dim[1][0]) and (point[1][1] > dim[1][1]):
                board[index] = value
            index += 1;

        
        
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), color , 2)
        last_pts.append(pt)


def getField(fieldTemplate):
    blockWidth, blockHeigth = fieldTemplate.shape[::-1]
    blockWidth /= 4
    blockHeigth /= 4
    res = cv2.matchTemplate(img_gray,fieldTemplate,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    pt = zip(*loc[::-1])[0]

    
    #print(blockWidth, blockHeigth)
    #for x in range(1,5):
    #    for y in range (1,5):
    #        #grid.append(pt)
    #        grid.append((pt ,(pt[0] + (blockWidth * x), pt[1] + (blockHeigth * y))))
            #cv2.rectangle(img_rgb , pt , (pt[0] + (blockWidth * x)  , pt[1] + (blockHeigth * y)), (125,125,125) , 2)

    pt2 = pt
    #for x in range (1,5):     
    #    for y in range (1,5):
    #        grid.append((pt, (pt[0] + blockWidth, pt[1] + (blockHeigth))))
    #        pt = (pt[0], (pt[1] + blockHeigth))
    #    pt = ((pt2[0] + (blockWidth * x)), pt2[1])

    for y in range (1,5):     
        for x in range (1,5):
            grid.append((pt, (pt[0] + blockWidth, pt[1] + (blockHeigth))))
            pt = ((pt[0] + (blockWidth), pt[1]))
        pt = (pt2[0], (pt2[1] + blockHeigth* y))
        

    drawGrid(grid)
        

def drawGrid(grid):
    for pt in grid:
        cv2.rectangle(img_rgb,pt[0], pt[1], (0,0,0), 2)
    
    

def printBoard(board):
    val = 0;
    for x in range(1,5):
        print(board[val],board[val+1],board[val+2],board[val+3])
        val += 4;

getField(template3)
getMatches(template,(0,255,0),2)
getMatches(template2,(255,0,0),4)
getMatches(template4,(125,0,125),8)
getMatches(template5,(0,125,125),16)

printBoard(board)

cv2.imwrite('res.png',img_rgb)
