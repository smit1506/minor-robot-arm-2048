import urx
import os
from time import sleep
from robot_controls import robot_positions
from robot_vision import vision
from robot_brain import weighted_table

# Set current path
path = '' if "App" in os.getcwd() else 'App'
board = None
rob = None
positions = None
direction = None


def init():
    global positions, rob
    # Connect to robot
    rob = urx.Robot("192.168.1.101")

    #leave some time to robot to process the setup commands
    sleep(0.2)

    # don't assign positions in positions text file twice if already not None
    positions = positions or robot_positions.positions(os.path.join(os.getcwd(), path, "robot_controls", "positions.txt"))

    #move robot to start position
    rob.movel(positions.get("start"), wait=False, vel=0.2, acc=0.5)

    # Run vision initialization when robot is on start position
    return vision.init()

def calibrate(position_name):
    global positions

    positions = positions or robot_positions.positions(os.path.join(os.getcwd(), path, "robot_controls", "positions.txt"))

    # Store current position with position_name in the text file
    positions.store(position_name)



# Just run, don't use interface
def run_standalone():
    # Do moves until no move is valid
    while (direction != -1):
        run()

    # Then move to start positions
    rob.movej(positions.get("start"), wait=True, vel=0.7, acc=1.1, pose=True)

    #done
    vision.releaseCamera()

def run():
    global direction

    # get next direction and do next move with the direction
    direction = getDirection()
    doMove(direction)
    return (direction, board)


# Go to center of screen and do next move
def doMove(direction):

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
    sleep(0.5)

def getDirection():
    global board
    updated = False
    last_board = board

    rob.movel(positions.get("start"), wait=False, vel=0.2, acc=0.5)
    sleep(3)
    # Use vision to get the latest board
    board = vision.updateBoard()
    if board is None:
        return -2
    print(board)

    # Use algorithm to get next move
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
