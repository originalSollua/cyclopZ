# keydrive - listen to keyboard, use it it move

#w forward
#s backwards
#a left
# d right
# space open / close
import curses
import serial
import time
import curses

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

        self.k_default_speed = 500
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

    def incleft(self):
        self.zerorot=self.zerorot+self.speed
        self.usb.write("#0 P"+str(self.zerorot)+" S"+str(self.k_default_speed)+" \r")
    def incright(self):
        self.zerorot=self.zerorot-self.speed
        self.usb.write("#0 P"+str(self.zerorot)+" S"+str(self.k_default_speed)+" \r")
    def incforward(self):
        self.onerot=self.onerot+self.speed
        self.usb.write("#1 P"+str(self.onerot)+" S"+str(self.k_default_speed)+" \r")
    def incbackward(self):
        self.onerot=self.onerot-self.speed
        self.usb.write("#1 P"+str(self.onerot)+" S"+str(self.k_default_speed)+" \r")
    def incup(self):
        self.tworot=self.tworot+self.speed
        self.usb.write("#2 P"+str(self.tworot)+" S"+str(self.k_default_speed)+" \r")
    def incdown(self):
        self.tworot=self.tworot-self.speed
        self.usb.write("#2 P"+str(self.tworot)+" S"+str(self.k_default_speed)+" \r")
    def incpanup(self):
        self.threerot=self.threerot+self.speed
        self.usb.write("#3 P"+str(self.threerot)+" S"+str(self.k_default_speed)+" \r")
    def incpandown(self):
        self.threerot=self.threerot-self.speed
        self.usb.write("#3 P"+str(self.threerot)+" S"+str(self.k_default_speed)+" \r")
    def open(self):
        self.fourrot=self.fourrot+self.speed
        self.usb.write("#4 P"+str(self.fourrot)+" S"+str(self.k_default_speed)+" \r")
    def close(self):
        self.fourrot=self.fourrot-self.speed
        self.usb.write("#4 P"+str(self.fourrot)+" S"+str(self.k_default_speed)+" \r")

inchar = 'm'

stdscr = curses.initscr()
curses.endwin()



c = cyclopzkeys()
stdscr = curses.initscr()
while not inchar == "p":
    inchar = stdscr.getkey()
    print 'you entered'+(inchar)
    if inchar =="w":
        c.incforward()
    if inchar =="s":
        c.incbackward()
    if inchar =="a":
        c. incleft()
    if inchar =="d":
        c.incright()
    if inchar == "q":
        c.incpanup()
    if inchar =="e":
        c.incpandown()
    if inchar == "v":
       c.open()
    if inchar == "c":
      c.close()
    if inchar == "z":
      c.incup()
    if inchar == "x":
      c.incdown()
print("done")
curses.endwin()
