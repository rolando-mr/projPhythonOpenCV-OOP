
from pkgproject.Camera import Camera
from pkgproject.ComSerial import ComSerial
from pkgproject.LineFollowerRobot import LineFollowerRobot

if __name__ == '__main__':

    configCamera = Camera(width=640, height=480, fps=30)
    camera = configCamera.configure_webcamera()

    computerCom = ComSerial()

    lineFollowerRobot = LineFollowerRobot(camera, computerCom)
    lineFollowerRobot.star()
