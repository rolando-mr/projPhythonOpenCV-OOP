from pkgproject.Camera import Camera
from pkgproject.ComSerial import ComSerial
from pkgproject.LineFollowerRobot import LineFollowerRobot


class Main:
    @staticmethod
    def init():
        config_camera = Camera(width=640, height=480, fps=30)
        camera = config_camera.configure_web_camera()

        computer_com = ComSerial()

        line_follower_robot = LineFollowerRobot(camera, computer_com)
        line_follower_robot.star()


if __name__ == '__main__':
    Main.init()
