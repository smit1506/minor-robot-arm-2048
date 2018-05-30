#template matching attempt
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

camera = None
img_rgb = None
img_gray = None
tiles = None
path = '' if __name__ == "__main__" else 'robot_vision/'
template_path = path + 'templates'
tile_path = template_path + '/tiles'
tile_info = [((0,255,0),2), ((255,0,0),4), ((125,0,125),8), ((0,125,125),16)]

grid = []
board = [0] * 16

def init():
    global camera, img_rgb, img_gray, tiles
    camera = cv2.VideoCapture(2)
    _, img_rgb  = camera.read()

    #img_rgb = cv2.imread(path + 'test5.jpg')
    #img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    tiles = os.listdir(tile_path)
    fieldTemplate = cv2.imread(template_path + '/template_field.png', 0)
    # cv2.imshow('t', fieldTemplate)
    # if cv2.waitKey(30000) & 0xFF == ord('q'):
    #     return
    getField(fieldTemplate)

def updateBoard():
    global img_rgb, img_gray
    # get matches and put them on board list
    img_rgb = cv2.imread('test12.jpg')
    # _, img_rgb  = camera.read()
    # cv2.imshow('frame',img_rgb)
    # if cv2.waitKey(30000) & 0xFF == ord('q'):
    #     return

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    getAllMatches()
    return normalizeBoard(board)

def getAllMatches():
    index = 0
    for tile in tiles:
       tile_template = cv2.imread(tile_path + '/' + tile, 0)
       #unpacks tile info at index and passes values as arguments
       getMatches(tile_template, *tile_info[index])
       index += 1



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



    next_pt = pt

    for y in range (1,5):
        for x in range (1,5):
            grid.append((pt, (pt[0] + blockWidth, pt[1] + (blockHeigth))))
            pt = ((pt[0] + (blockWidth), pt[1]))
        pt = (next_pt[0], (next_pt[1] + blockHeigth* y))


    drawGrid(grid)


def drawGrid(grid):
    for pt in grid:
        cv2.rectangle(img_rgb,pt[0], pt[1], (0,0,0), 2)



def normalizeBoard(board):
    result = [[],[],[],[]]
    val = 0;
    for x in range(0,4):
        result[x] = [board[val],board[val+1],board[val+2],board[val+3]]
        val += 4;
    return result

def releaseCamera():
    camera.realease()

# printBoard(board)
init()
# print updateBoard()
#getAllMatches()
print updateBoard()
cv2.imwrite('res.png',img_rgb)
