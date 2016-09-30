# initialization module. 
# call to initialize variable and imports
import serial
import time
from cv2.cv import *
#import picamera
#import picamera.array
class cyclopz:
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
        self.k_trash_pile = 500
        self.k_yellow_pile = 1000
        self.k_pile_pile = 1500
        self.k_pink_pile = 2000
        self.k_red_pile = 2500

        self.k_default_speed = 500
        self.k_default_shoulder = 1500
        self.k_default_elbow = 1500
        self.k_default_wrist = 1500
        self.k_default_hand = 1500
        self.count = 1

        try:
            self.usb.open()
        except serial.SerialException:
            self.usb.close()
            self.usb.open()
        else:
            print("error opening usb")

        self.usb.write("#1 P"+str(self.k_default_shoulder)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#2 P"+str(self.k_default_elbow)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#3 P"+str(self.k_default_wrist)+" S"+str(self.k_default_speed)+" \r") 
        self.usb.write("#4 P"+str(self.k_default_hand)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#0 P"+str(self.k_pile_pile)+" S"+str(self.k_default_speed)+" \r")

    def test(self):
        #test rotational base
        self.usb.write("#0 P"+str(self.k_red_pile)+"  S"+str(self.k_default_speed)+" \r")
        time.sleep(6)
        self.usb.write("#0 P"+str(self.k_yellow_pile)+"  S"+str(self.k_default_speed)+" \r")
        time.sleep(6)
        self.usb.write("#0 P"+str(self.k_pink_pile)+"  S"+str(self.k_default_speed)+" \r")
        time.sleep(6)
        self.usb.write("#0 P"+str(self.k_trash_pile)+" S"+str(self.k_default_speed)+" \r")
        time.sleep(6)
        self.usb.write("#0 P"+str(self.k_red_pile)+"  S"+str(self.k_default_speed)+" \r")
        time.sleep(6)
    def terminate(self):
        self.usb.close()

    def move_to_trash(self):
        self.usb.write("#1 P"+str(self.k_default_shoulder)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#2 P"+str(self.k_default_elbow)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#0 P"+str(self.k_trash_pile)+" S"+str(self.k_default_speed)+" \r") 
        time.sleep(3)
        self.usb.write("#1 P900 S"+str(self.k_default_speed)+" \r")
        time.sleep(1)
        self.usb.write("#3 P1000 S"+str(self.k_default_speed)+" \r") 
        time.sleep(1)
    def move_to_red(self):
        self.usb.write("#1 P"+str(self.k_default_shoulder)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#2 P"+str(self.k_default_elbow)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#0 P"+str(self.k_red_pile)+" S"+str(self.k_default_speed)+" \r") 
        time.sleep(3)
        self.usb.write("#1 P1300 S"+str(self.k_default_speed)+" \r")
        time.sleep(1)
        self.usb.write("#3 P900 S"+str(self.k_default_speed)+" \r") 
        time.sleep(1)
    def move_to_yellow(self):
        self.usb.write("#1 P"+str(self.k_default_shoulder)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#2 P"+str(self.k_default_elbow)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#0 P"+str(self.k_yellow_pile)+" S"+str(self.k_default_speed)+" \r") 
        time.sleep(3)
        self.usb.write("#1 P1300 S"+str(self.k_default_speed)+" \r")
        time.sleep(1)
        self.usb.write("#3 P900 S"+str(self.k_default_speed)+" \r") 
        time.sleep(1)
    def move_to_pink(self):
        self.usb.write("#1 P"+str(self.k_default_shoulder)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#2 P"+str(self.k_default_elbow)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#0 P"+str(self.k_pink_pile)+" S"+str(self.k_default_speed)+" \r") 
        time.sleep(3)
        self.usb.write("#1 P1300 S"+str(self.k_default_speed)+" \r")
        time.sleep(1)
        self.usb.write("#3 P900 S"+str(self.k_default_speed)+" \r") 
        time.sleep(1)
    def move_to_home(self):
        self.usb.write("#1 P"+str(self.k_default_shoulder)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#2 P"+str(self.k_default_elbow)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#0 P"+str(self.k_pile_pile)+" S"+str(self.k_default_speed)+" \r") 
        self.usb.write("#4 P"+str(self.k_default_hand)+"  S"+str(self.k_default_speed)+" \r")
        time.sleep(2)
    def rake(self):
        #line up arm wit pile
        self.usb.write("#0 P"+str(self.k_pile_pile)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#1 P1025 S200 \r")
        self.usb.write("#2 p1500 S200 \r")
        time.sleep(1)
        #dive te arm into the pile
        self.usb.write("#3 p1000 S200 \r")
        self.usb.write("#4 p1000 S300 \r")
        time.sleep(3)
        #draw arm back through pile
        i = 1025
        j = 1500
        while not self.test_image() and i <= 2000 and j <= 2500:
            self.usb.write("#1 P"+str(i+7)+" S100 \r")
            self.usb.write("#2 P"+str(j+26)+" S125 \r")
            time.sleep(.1)
            i = i+5
            j = j+10
        self.usb.write("#4 p7500 S300 \r")
        time.sleep(3)
    
    def rotLeft(self):
        self.usb.write("#0 P"+str(self.k_pile_pile-self.count*20)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#2 p1500 S200 \r")
        self.count=self.count+1
        time.sleep(4)
    def rotRight(self):
        self.usb.write("#0 P"+str(self.k_pile_pile+self.count*20)+" S"+str(self.k_default_speed)+" \r")
        self.usb.write("#2 p1500 S200 \r")
        self.count=self.count+1
        time.sleep(4)
    def test_image(self):
        pass
        return False

print("hear we go")
a = cyclopz()
time.sleep(6)
#a.test()
#time.sleep(2)
#a.move_to_trash()
#time.sleep(3)
#a.move_to_red()
#time.sleep(3)
#a.move_to_yellow()
#time.sleep(3)
#a.move_to_pink()
while a.count < 15:
    a.move_to_home()
    a.rake()
    a.move_to_home()
    a.rotLeft()
    a.rake()
    a.move_to_home()
    a.rotRight()
