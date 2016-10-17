# keydrive - listen to keyboard, use it it move

#w forward
#s backwards
#a left
# d right
# space open / close
import serial

class cyclopzkeys:
    def __init__(self):
        self.usb = serial.Serial(
                port='/dev/ttyUSB0',
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                xonxoff=serial.XOFF,
                rtscts=False,
                dsrdtr=False
                )

        self.k_default_speed = 750
        self.k_default_shoulder = 1500
        self.k_default_elbow = 1500
        self.k_default_wrist = 1500
        self.k_default_hand =700
        self.speed = 20   
        self.zerorot = 1500
        self.onerot = self.k_default_shoulder
        self.tworot = self.k_default_elbow
        self.threerot = self.k_default_wrist
        self.fourrot = self.k_default_hand
        self.max = 2500
        self.min = 0
       
        try:
            self.usb.open()
        except serial.SerialException:
            self.usb.close()
            self.usb.open()
        else:
            print("error opening usb")

        self.usb.write("#1 P"+str(self.k_default_shoulder)+" S100 \r")
        self.usb.write("#2 P"+str(self.k_default_elbow)+" S100 \r")
        self.usb.write("#3 P"+str(self.k_default_wrist)+" S100 \r") 
        self.usb.write("#4 P"+str(self.k_default_hand)+" S100 \r")

    def inc_base_rotation(self, x):
        self.zerorot = self.zerorot+int(round(x))
        if self.zerorot < 0:
            self.zerorot = 0
        if self.zerorot > 2500:
            self.zerorot = 2500
        self.usb.write("#0 P"+str(self.zerorot)+" S"+str(self.k_default_speed)+" \r")
    def inc_shoulder_angle(self,y):
        self.onerot = self.onerot-int(round(y))
        if self.onerot < 0:
            self.onerot = 0
        if self.onerot > 2500:
            self.onerot = 2500
        self.usb.write("#1 P"+str(self.onerot)+" S"+str(self.k_default_speed)+" \r")
    def inc_elbow_angle(self, x):
        self.tworot = self.tworot+int(round(x))
        if self.tworot < 0:
            self.tworot = 0
        if self.tworot > 2500:
            self.tworot = 2500
        self.usb.write("#2 P"+str(self.tworot)+" S"+str(self.k_default_speed)+" \r")
    def inc_wrist_angle(self, y):
        self.threerot = self.threerot-int(round(y))
        #adjust these valuse to stop popping the camera off the pi
        if self.threerot < 0:
            self.threerot = 0
        if self.threerot > 1200:
            self.threerot = 1200
        self.usb.write("#3 P"+str(self.threerot)+" S"+str(self.k_default_speed)+" \r")
    def open(self):
        self.usb.write("#4 P500 S"+str(self.k_default_speed)+" \r")
    def close(self):
        self.usb.write("#4 P2000 S"+str(self.k_default_speed)+" \r")
	

