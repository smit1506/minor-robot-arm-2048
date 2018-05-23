import urx
from time import sleep
from record_position import recordposition

rob = urx.Robot("192.168.1.101")

print("Connected")

sleep(0.2)  #leave some time to robot to process the setup commands

positions = recordposition("D:/Documents/Minors/Robotarm/Programs/2048/positions.txt")

for x in range(0, 2):
    rob.movej(positions.get("test1"), wait=True, vel=0.7, acc=1.1, pose=True)
    rob.movej(positions.get("test2"), wait=True, vel=0.7, acc=1.1, pose=True)

print("Done")
