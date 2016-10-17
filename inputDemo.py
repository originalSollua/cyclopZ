from reader import SixAxis
import time
from keydrive import cyclopzkeys
controler = SixAxis(dead_zone = 0.0, hot_zone = 0.00, connect=True)
exit = False
def handler(button):
    print 'Button!!!! {}'.format(button)
def handler_exit(button):
    controler.disconect()
prevx = 0
prevy = 0
controler.register_button_handler(handler, SixAxis.button_circle)
controler.register_button_handler(handler_exit, SixAxis.button_ps)
c = cyclopzkeys()
current_milli_time = lambda: int(round(time.time()*10))
last_time = current_milli_time()

while controler.is_connected():
    #controler.handle_event()
    x = controler.axes[0].corrected_value()
    y = controler.axes[1].corrected_value()
    c.inc_base_rotation(10*x)
    c.inc_shoulder_angle(10*y)
     
    x = controler.axes[2].corrected_value()
    y = controler.axes[3].corrected_value()
    c.inc_elbow_angle(10*x)
    c.inc_wrist_angle(10*y)
    now = current_milli_time()
    if now > (last_time + 100):
        last_time = now

