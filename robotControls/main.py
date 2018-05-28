import urx
from time import sleep
from record_position import recordposition

rob = urx.Robot("192.168.1.101")

print("Connected")

sleep(0.2)  #leave some time to robot to process the setup commands

positions = recordposition("D:/Documents/Minors/Robotarm/Programs/2048/positions.txt")

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

print("Done")
