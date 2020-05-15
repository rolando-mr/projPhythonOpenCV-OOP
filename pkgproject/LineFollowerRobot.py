import cv2

from pkgproject.ProcImage import ProcImage


class LineFollowerRobot:
    """
    esta clase se encarga de capturar las imagenes, pasarlas
    para analizar y despues envia el correspondiente mensaje
     atravez del puerto serie
    """
    theta = 0
    threshold = 6

    def __init__(self, camera, com_serial):
        self.camera = camera
        self.com_serial = com_serial

    def star(self):
        while True:
            # for frame in camera.capture_continuous (rawCapture, format = "bgr", use_video_port = True):
            try:
                # grabbed,frame=frame.array
                grabbed, frame = self.camera.read()
                if grabbed:
                    cv2.imshow('Video', frame)

                    theta, image = ProcImage.process_image(frame)
                    self.com_serial.go_forward_to(self.threshold, theta)
                    theta = 0

                    cv2.imshow("Frame", image)
                    if cv2.waitKey(1) == ord('q'):
                        # Press Q on keyboard to  exit
                        print("Transmisión detenida debido a evento de tecla presionada")
                        self.com_serial.stop_go_forward_to()
                        break

            except KeyboardInterrupt:
                self.com_serial.stop_go_forward_to()
        # Closes all the frames
        cv2.destroyAllWindows()
