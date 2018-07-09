#template matching attempt
import os
import cv2
import urllib2
from time import sleep
import numpy as np
from matplotlib import pyplot as plt

img_rgb = None
img_gray = None
tiles = None
ip = "192.168.1.101"
url = "http://" + ip + ":4242/current.jpg?type=color"
cwd = os.getcwd()
cwd = cwd if 'App' in cwd else os.path.join(cwd, 'App')
path = cwd if "robot_vision" in cwd else os.path.join(cwd, 'robot_vision')
template_path = os.path.join(path, 'templates')
tile_path = os.path.join(template_path, 'tiles')
tile_info = [0] + [1 << i for i in range(1, 15)]

grid = []
board = [0] * 16

#Initiates the vision class
def init():
    global  img_rgb, img_gray, tiles

    _ = urllib2.urlopen("http://" + ip + ":4242/setdisplaysize?width=1280&height=720").read()
    sleep(3)
    img_rgb = getCameraImage()
    tiles = os.listdir(tile_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    field_template = cv2.imread(os.path.join(template_path, 'template_field_cropped.png'), 0)
    if not getField(field_template):
        return False
    print "Found field"
    return True

#Used to update the game board
#It takes a new image from the camera and calls the getAllMatches() function
def updateBoard():
    global img_rgb, img_gray

    sleep(3)
    img_rgb  = getCameraImage()
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    if getAllMatches():
        return normalizeBoard(board)
    else:
        return None

#Used to get an image from the camera
def getCameraImage():
    _, image = cv2.VideoCapture(url).read()
    cv2.imwrite(os.path.join(path, os.pardir, os.pardir, os.pardir, 'interface', 'cam.png'),image)
    return image

#Used to pass tile templates to the getMatches method.
def getAllMatches():
    templates = []
    index = 0
    for tile in tiles:
        tile_template = cv2.imread(os.path.join(tile_path, tile), 0)
        templates.append((tile_template, tile_info[index]))
        index += 1
    if not getMatches(templates,grid):
        return False
    return True

#used to get the value of each game tile based on the given templates and grid
#Tiles will be calculated based on the grid's dimensions
#Each tile is then checked for template matches, the best match for a tile is picked
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
        if len(board) < index:
            return False
        board[index] = best_value
        if best_value > 0:
            cv2.rectangle(img_rgb,point[0],point[1],(255,0,0),2)
        index += 1
    return True

#Used to create a field template based on coordinates from the web interfaceself
#The field template will be cropped from the original image
def getFieldTemplate(rct):
    print(rct)
    if (sum(rct) == 0):
        return False
    img_crop = img_gray[int(rct[1]):int(rct[1]+rct[3]), int(rct[0]):int(rct[0]+rct[2])]
    cv2.imwrite(os.path.join(template_path, 'template_field_cropped.png'), img_crop)
    cv2.imwrite(os.path.join(path, os.pardir, os.pardir, os.pardir, 'interface', 'template_field_cropped.png'),img_crop)
    return getField(img_crop)


#Used to find the playing field based on the field template
#If a match above the threshold is found, a grid will be made based on the match coordinates
def getField(field_template):
    if field_template is None:
        return False
    block_width, block_height = field_template.shape[::-1]
    block_width /= 4
    block_height /= 4
    res = cv2.matchTemplate(img_gray,field_template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    loc = np.where(res >= threshold)
    loc_list = zip(*loc[::-1])
    if len(loc_list) == 0:
        print("No field template found. Select new template.")
        return False

    pt = loc_list[0]

    next_pt = pt

    #creates a 4*4 grid based on points from the found playing field
    for y in range (1,5):
        for x in range (1,5):
            grid.append((pt, (pt[0] + block_width, pt[1] + (block_width))))
            pt = ((pt[0] + (block_width), pt[1]))
        pt = (next_pt[0], (next_pt[1] + block_height* y))


    drawGrid(grid)
    return True

#Draws a 4*4 grid
#Used to verify the location of the grid
def drawGrid(grid):
    for pt in grid:
        cv2.rectangle(img_rgb,pt[0], pt[1], (0,0,0), 2)
    print "Drawing template field"
    print (os.path.join(path, os.pardir, os.pardir, os.pardir, 'interface', 'template_field.png'))
    cv2.imwrite(os.path.join(template_path, 'template_field.png'), img_rgb)
    cv2.imwrite(os.path.join(path, os.pardir, os.pardir, os.pardir, 'interface', 'template_field.png'),img_rgb)


#Creates a 4*4 playing field
def normalizeBoard(board):
    result = [[],[],[],[]]
    val = 0;
    for x in range(0,4):
        result[x] = [board[val],board[val+1],board[val+2],board[val+3]]
        val += 4;
    return result

# Path should be empty if running module standalone
if path == cwd:
    init()
    print(updateBoard())
    cv2.imwrite(os.path.join(path, 'res.png'),img_rgb)
