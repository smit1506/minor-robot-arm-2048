import urx
import os
from time import sleep
from robot_controls import robot_positions
from robot_vision import vision
from robot_brain import weighted_table

path = '' if "App" in os.getcwd() else 'App'
board = None
rob = None
positions = None
direction = None
def calibrate(position_name):
    global positions
    positions = robot_positions.positions(os.path.join(os.getcwd(), path, "robot_controls", "positions.txt"))
    positions.store(position_name)

def init():
    global positions, rob
    rob = urx.Robot("192.168.1.101")
    #print("Connected")

    sleep(0.2)  #leave some time to robot to process the setup commands
    # don't assign same object to positions twice if already not None
    positions = positions or robot_positions.positions(os.path.join(os.getcwd(), path, "robot_controls", "positions.txt"))
    rob.movel(positions.get("start"), wait=False, vel=0.2, acc=0.5)
    #sleep(5)
    return vision.init()

def run_standalone():
    while (direction != -1):
        #direction = getDirection()
        #print(direction)
        doMove(getDirection())
    rob.movej(positions.get("start"), wait=True, vel=0.7, acc=1.1, pose=True)

    # loop
    doMove(getDirection())
    # wait until robot has moved and repeat

    #done
    vision.releaseCamera()

def run():
    global direction
    direction = getDirection()
    doMove(direction)
    return (direction, board)

def doMove(direction):

    #go to center of screen and do move
    rob.movel(positions.get("center"), wait=False, vel=0.2, acc=0.5)
    sleep(1)
    if direction == 0:
        rob.movel(positions.get("left"), wait=False, vel=0.2, acc=0.5)
        print("Left!")
    elif direction == 1:
        rob.movel(positions.get("up"), wait=False, vel=0.2, acc=0.5)
        print("Up!")
    elif direction == 2:
        rob.movel(positions.get("right"), wait=False, vel=0.2, acc=0.5)
        print("Right!")
    elif direction == 3:
        rob.movel(positions.get("down"), wait=False, vel=0.2, acc=0.5)
        print("Down!")
    sleep(1)

def getDirection():
    global board
    updated = False
    last_board = board

    rob.movel(positions.get("start"), wait=False, vel=0.2, acc=0.5)
    sleep(2)
    board = vision.updateBoard()
    if board is None:
        return -2
    print(board)
    return weighted_table.getMove(board, 4)

def goToStart():
    global rob, positions
    positions = positions or robot_positions.positions(os.path.join(os.getcwd(), path, "robot_controls", "positions.txt"))
    rob = urx.Robot("192.168.1.101")
    rob.movel(positions.get("start"), wait=False, vel=0.2, acc=0.5)
    print("Moving to start")

def setFieldTemplate(rct):
    return vision.getFieldTemplate(rct)

def getCameraImage():
    vision.getCameraImage()

if 'App' not in path:
    init()
    run_standalone()
