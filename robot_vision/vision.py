#template matching attempt
import os
import cv2
import urllib2
from time import sleep
import numpy as np
from matplotlib import pyplot as plt

camera = None
img_rgb = None
img_gray = None
tiles = None
ip = "141.252.128.6"
url = "http://" + ip + ":4242/current.jpg?type=color"
path = '' if "robot_vision" in os.getcwd() else 'robot_vision/'
template_path = path + 'templates'
tile_path = template_path + '/tiles'
tile_info = [0] + [1 << i for i in range(1, 15)]

grid = []
board = [0] * 16

def init():
    global camera, img_rgb, img_gray, tiles

    _ = urllib2.urlopen("http://" + ip + ":4242/setdisplaysize?width=1280&height=720").read()
    camera = cv2.VideoCapture("")
    #camera = cv2.VideoCapture(1)
    sleep(3)
    # UNCOMMENT THIS WHEN ACTUAL CAM IS CONNECTED
    _, img_rgb  = getCameraImage()
    #img_rgb = cv2.imread(path + 'cam.png')

    cv2.imwrite(path + 'cam.png',img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    tiles = os.listdir(tile_path)
    field_template = cv2.imread(template_path + '/template_field.png', 0)
    getField(field_template)

def updateBoard():
    global img_rgb, img_gray

    # UNCOMMENT THIS WHEN ACTUAL CAM IS CONNECTED
    sleep(3)
    _, img_rgb  = getCameraImage()
    #img_rgb = cv2.imread(path + 'cam.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("board",img_gray)
    # cv2.waitKey(0)
    getAllMatches()
    return normalizeBoard(board)

def getCameraImage():
    return cv2.VideoCapture(url).read()

def getAllMatches():
    templates = []
    index = 0
    for tile in tiles:
        tile_template = cv2.imread(tile_path + '/' + tile, 0)
        templates.append((tile_template, tile_info[index]))
        index += 1
    getMatches(templates,grid)


def getMatches(templates,grid):
    threshold = 0.1
    index = 0
    for point in grid:
        grid_fragment = img_gray[point[0][1]:point[1][1], point[0][0]:point[1][0]]
        best_accuracy = 0
        best_value = 0

        for template in templates:
            res = cv2.matchTemplate(grid_fragment, template[0], cv2.TM_CCOEFF_NORMED)
            accuracy = np.amax(res)
            loc = np.where(res >= threshold)
            loc_list = zip(*loc[::-1])
            if len(loc_list) == 0:
                continue
            if best_accuracy < accuracy:
                best_accuracy = accuracy
                best_value = template[1]

                # print("VALUE: "+str(template[2])+" BETTER ACCURACY:"+str(accuracy))
            # else:
            #     print("VALUE: "+str(template[2])+" WORSE ACCURACY:"+str(accuracy))
        board[index] = best_value
        if best_value > 0:
            cv2.rectangle(img_rgb,point[0],point[1],(255,0,0),2)
        index += 1


def getFieldTemplate(image):
    r = cv2.selectROI("Image",image,False,False)
    if (sum(r) == 0):
        print ("Nothing selected. Restart the script.")
        exit(0)
    img_crop = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    if (img_crop == []):
        print ("IMG CROP")
        print (img_crop)
    cv2.imwrite(template_path + '/template_field.png', img_crop)
    return img_crop

def getField(field_emplate):
    block_width, block_height = field_emplate.shape[::-1]
    block_width /= 4
    block_height /= 4
    res = cv2.matchTemplate(img_gray,field_emplate,cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    loc = np.where(res >= threshold)
    loc_list = zip(*loc[::-1])
    if len(loc_list) == 0:
        print("No field template found. Select new template.")
        return getField(getFieldTemplate(img_gray))
    pt = loc_list[0]

    next_pt = pt

    for y in range (1,5):
        for x in range (1,5):
            grid.append((pt, (pt[0] + block_width, pt[1] + (block_width))))
            pt = ((pt[0] + (block_width), pt[1]))
        pt = (next_pt[0], (next_pt[1] + block_height* y))


    drawGrid(grid)


def drawGrid(grid):
    for pt in grid:
        cv2.rectangle(img_rgb,pt[0], pt[1], (0,0,0), 2)
    cv2.imshow('drawGrid',img_rgb)
    if cv2.waitKey(30000) & 0xFF == ord('q'):
        sleep(1)


def normalizeBoard(board):
    result = [[],[],[],[]]
    val = 0;
    for x in range(0,4):
        result[x] = [board[val],board[val+1],board[val+2],board[val+3]]
        val += 4;
    return result

def releaseCamera():
    camera.release()

# Path should be empty if running module standalone
if path == '':
    init()
    print(updateBoard())
    cv2.imwrite('res.png',img_rgb)
    releaseCamera()
