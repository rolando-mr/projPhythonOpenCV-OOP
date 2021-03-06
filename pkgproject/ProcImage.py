import math

import cv2
import numpy as np


class ProcImage:
    """
    ProcImage toma una imagen luego lo analiza, realiza los calculos de las lineas
    y devuelve los resultados
    """
    minLineLength = 5
    maxLineGap = 10

    @staticmethod
    def process_image(frame, min_line_length=5, max_line_gap=10):
        theta = 0
        image = frame  # frame.array (picamera)
        #image = cv2.imread(r'images/dir_derecha.png') # para probar con fotos descomentar y agregar r'images/name_img.png'
        image = cv2.resize(image, (500, 300))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 85, 85)
        lines = cv2.HoughLinesP(edged, 1, np.pi / 180, 10, min_line_length, max_line_gap)
        for x in range(0, len(lines)):
            for x1, y1, x2, y2 in lines[x]:
                cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                theta = theta + math.atan2((y2 - y1), (x2 - x1))
                # print(theta)
        return theta, image
