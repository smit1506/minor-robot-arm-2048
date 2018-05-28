import urx
from time import sleep
from robotControls import record_position # why was this here?
from robotVision import vision

#rob = urx.Robot("192.168.1.101")
#print("Connected")

sleep(0.2)  #leave some time to robot to process the setup commands

positions = record_position.recordposition("D:/Documents/Minors/Robotarm/Programs/2048/robotControls/positions.txt")

board = None

def main():
    vision.init()
    # loop
    doMove(getDirection())
    # wait until robot has moved and repeat

def doMove(direction):
    rob.movej(positions.get("center"), wait=True, vel=0.7, acc=1.1, pose=True)
    # if movement should be to the left
    if direction == 1:
        rob.movej(positions.get("left"), wait=True, vel=0.7, acc=1.1, pose=True)
    elif direction == 2:
        rob.movej(positions.get("up"), wait=True, vel=0.7, acc=1.1, pose=True)
    elif direction == 3:
        rob.movej(positions.get("right"), wait=True, vel=0.7, acc=1.1, pose=True)
    elif direction == 4:
        rob.movej(positions.get("down"), wait=True, vel=0.7, acc=1.1, pose=True)

def getDirection():
    board = vision.updateBoard()
    print board
    # give board to AI to get next move

getDirection()
print("Done")
