import urx
from time import sleep
from record_position import recordposition
from parsegcode import parsegcode


rob = urx.Robot("141.252.128.7")
sleep(0.2)  #leave some time to robot to process the setup commands

print("Connected")
# print(rob.getl())

positions = recordposition("C:/Users/Mark Snijder/Google Drive/NHL/Jaar 3/Minor/UR5Share/Robista/test.txt") #Position file

leftUpperCorner = positions.get("leftUpper")
leftBottomCorner = positions.get("leftBottom")
rightBottomCorner = positions.get("rightBottom")
rightBottomCorner[2] = leftBottomCorner[2]  #To make sure it's exactly horizontal

# rob.movej(leftBottomCorner, pose=True)

parser = parsegcode("C:/Users/Mark Snijder/Documents/Pepe.nc", leftUpperCorner, rightBottomCorner, leftBottomCorner) #GCode file

parser.toRobotCoordinates()

arrayOfArray = []
for coordinate3D in parser.coordinates3D:
    arrayOfArray.append((coordinate3D.x, coordinate3D.y, coordinate3D.z, leftBottomCorner[3], leftBottomCorner[4], leftBottomCorner[5]))

rob.movels(arrayOfArray, acc=0.6, vel=1.0, radius=0.005, wait=False)
