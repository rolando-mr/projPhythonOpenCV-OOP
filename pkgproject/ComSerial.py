class ComSerial:
    """
    Esta clase realiza las comunicacnion atravez de puerto serie
    a un microcontrolador y este pueda realizar alguna accion
    """
    timeout = 1

    # threshold = 6
    def __init__(self):
        # serialPort = serial.Serial("/dev/ttyACM0", 115200, timeout=1)           # linux
        pass

    """"
    def __init__(self,Port,baudios):
        self.serialPort=serial.Serial(Port, baudios, self.timeout)  # linux
    """

    def go_forward_to(self, threshold, theta):
        threshold = threshold
        if theta > threshold:
            # self.serialPort.write(chr(3).encode())
            print("Izquierda")
        if theta < -threshold:
            # self.serialPort.write(chr(2).encode())
            print("Derecha")
        if abs(theta) < threshold:
            # self.serialPort.ser.write(chr(1).encode())
            print("Avanzar")
        theta = 0

    def stop_go_forward_to(self):
        # self.self.serialPort.ser.write(chr(4).encode())
        print("Detenerse")
