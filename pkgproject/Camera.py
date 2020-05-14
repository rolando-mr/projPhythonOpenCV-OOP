import time

import cv2


class Camera:
    """
    Esta clase inicia una de las camera
    configure_RPI_camera() -> si se usa una raspberry pi camera
    configure_webcamera() -> si usa una webcam
    """

    def __init__(self, width=640, height=480, fps=30):
        self.width = width
        self.height = height
        self.fps = fps

    def configure_RPI_camera(self):
        # camera = picamera.PiCamera()
        # camera.resolution = (self.width, self.height)
        # camera.framerate = self.fps
        # rawCapture = picamera.array.PiRGBArray(camera, size = (self.width, self.height))
        # time.sleep (0.1)
        # return camera
        pass

    def configure_webcamera(self):
        camera = cv2.VideoCapture(0)
        camera.set(int(3), self.width)
        camera.set(int(4), self.height)
        camera.set(int(5), self.fps)
        time.sleep(0.1)
        return camera
