import urx
import sys
import os
from time import sleep


class positions:

    def __init__(self, filePath):
        print("Attempting to open: " + filePath)
        self.load(filePath)

    def load(self, filePath):
        self.filePath = filePath
        self.file = open(self.filePath, "r")
        self.lines = {}

        for storedPosition in self.file.readlines():
            split = storedPosition[:-1].split(",") #Remove newline and split on comma
            if len(split) == 7:
                self.lines[split[0]] = float(split[1]), float(split[2]), float(split[3]), float(split[4]), float(split[5]), float(split[6])

        self.file.close()

    def get(self, positionName):
        if positionName in self.lines:
            return self.lines[positionName]
        return None

    def store(self, name, x=None, y=None, z=None, rx=None, ry=None, rz=None):
        if x is None:
            rob = urx.Robot("192.168.1.101")
            pos = rob.getl()
            self.store(name, pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])
            return
        self.lines[name] = (x, y, z, rx, ry, rz)
        file = open(self.filePath, "w")

        for storedPosition in self.lines:
            file.write(storedPosition + "," + ",".join(map(str, self.lines[storedPosition])) + "\n")

        file.close()

if __name__ == "__main__":
    #py -2.7 .\record_position.py "C:\Users\Mark Snijder\PycharmProjects\Robista\test.txt"
    #rec = positions(sys.argv[1])
    rec = positions(os.path.join(os.getcwd(), "positions.txt"))

    rob = urx.Robot("141.252.128.6")
    sleep(0.2)  #leave some time to robot to process the setup commands

    while(True):
        positionName = raw_input("Move the robot to the desired position and enter a variable name. Or close to close: ")
        if positionName == "close":
            break

        rec.store(positionName)

    sys.exit()
