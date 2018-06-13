import urx
from time import sleep
from robot_controls import robot_positions
from robot_vision import vision
from robot_brain import weighted_table

rob = urx.Robot("141.252.128.6")
#print("Connected")

sleep(0.2)  #leave some time to robot to process the setup commands

positions = robot_positions.positions("D:/Documents/Minors/Robotarm/Programs/2048/robot_controls/positions.txt")

board = None

def main():

    rob.movel(positions.get("start"), wait=False, vel=0.2, acc=0.5)
    #sleep(5)
    vision.init()
    direction = None
    while (direction != -1):
        #direction = getDirection()
        #print(direction)
        doMove(getDirection())
    #rob.movej(positions.get("start"), wait=True, vel=0.7, acc=1.1, pose=True)
    # loop
    #doMove(getDirection())
    # wait until robot has moved and repeat

    #done
    vision.releaseCamera()

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
    sleep(1)
    board = vision.updateBoard()
    print(board)
    return weighted_table.getMove(board, 4)


main()
print("Done")
