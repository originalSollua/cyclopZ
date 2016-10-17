from asyncore import file_dispatcher, loop
import evdev
from evdev import InputDevice, list_devices, ecodes
from threading import Thread

class PsInputManager:
    def __init__(self, dead_zone=0.05, hot_zone=0.0):
        self.dead_zone = dead_zone
        self.hot_zone = hot_zone
    def __enter__(self):
        self.joystick = SixAxis(dead_zone = self.deadzone, hot_zone = self.hot_zone)
        self.jostick.connect()
        return self.joystick
    def __exit__(self):
        self.joystick.disconnect()

class SixAxis:
    ec_select = 288
    ec_start = 291
    ec_left_stick = 289
    ec_right_stick = 290
    ec_d_left = 295
    ec_d_right = 293
    ec_d_up = 292
    ec_d_down = 294
    ec_PS = 704
    ec_square = 303
    ec_triangle = 300
    ec_circle = 301
    ec_cross = 302
    ec_r1 = 299
    ec_r2 = 297
    ec_l1 = 298
    ec_l2 = 296

    ec_leftx = 0
    ec_lefty = 1
    ec_rightx = 2
    ec_righty = 5

    button_select = 0
    button_start = 1
    button_left_stick = 2
    button_right_stick = 3
    button_d_up = 4
    button_d_down = 5
    button_d_left = 6
    button_d_right = 7
    button_triangle = 8
    button_square = 9
    button_cross = 10
    button_circle = 11
    button_l1 = 12
    button_l2 = 13
    button_r1 = 14
    button_r2 = 15
    button_ps = 16

    def __init__(self, dead_zone=0.05, hot_zone =0.0, connect=False):
        self._stop_function=None
        self.axes = [SixAxis.Axis('left_x', dead_zone=dead_zone, hot_zone=hot_zone),
                     SixAxis.Axis('left_y', dead_zone=dead_zone, hot_zone=hot_zone),
                     SixAxis.Axis('right_x', dead_zone=dead_zone, hot_zone=hot_zone),
                     SixAxis.Axis('right_y', dead_zone=dead_zone, hot_zone=hot_zone)]
        self.button_handlers = []
        self.button_pressed = 0
        if connect:
            self.connect()

    def is_connected(self):
        if self._stop_function:
            return True
        else:
            return False

    def get_and_clear_button_press_history(self):
        old_buttons  =self.button_pressed
        self.button_pressed = 0
        return old_buttons

    def connect(self):
        if self._stop_function:
            return False
        for device in [InputDevice(fn) for fn in list_devices()]:
                print(device.name)
                if device.name =='PLAYSTATION(R)3 Controller':
                    parent = self
                
                class InputDeviceDispatcher(file_dispatcher):
                    def __init__(self):
                        self.device = device
                        file_dispatcher.__init__(self,device)

                    def recv(self, ign=None):
                        return self.device.read()
                    def handle_read(self):
                        for event in self.recv():
                            parent.handle_event(event)
                    def handle_error(self):
                        pass

                class AsyncLoop(Thread):
                    def __init__(self, channel):
                        Thread.__init__(self, group=None, name='InputDIspatchThread')
                        self.daemon = True
                        self.channel =channel

                    def run(self):
                        loop()
                    
                    def stop(self):
                        self.daemon = False
                        self.channel.close()

                loop_thread = AsyncLoop(InputDeviceDispatcher())
                self._stop_function = loop_thread.stop
                loop_thread.start()
                return True
        raise IOError('Cannot find controler')

    def disconnect(self):
        if self._stop_function:
            self._stop_function()
            self._stop_functio = None

    def __str__(self):
        return str(self.is_connected())

    def register_button_handler(self, button_handler, buttons):
        mask = 0
        if isinstance(buttons, list):
            for button in buttons:
                mask +=1 <<button
        else:
            mask += 1 <<buttons
        h = {'handler':button_handler,
             'mask':mask}
        self.button_handlers.append(h)
        
        def remove():
            self.button_handlers.remove(h)
            return remove

    def handle_event(self, event):
        if event.type == ecodes.EV_ABS:
            value = float(event.value) / 255.0
            if value < 0:
                value = 0
            elif value > 1.00:
                value = 1.00
            if event.code == SixAxis.ec_leftx:
                self.axes[0]._set(value)
            elif event.code ==SixAxis.ec_lefty:
                self.axes[1]._set(value)
            elif event.code == SixAxis.ec_rightx:
                self.axes[2]._set(value)
            elif event.code == SixAxis.ec_righty:
                self.axes[3]._set(value)
        elif event.type == ecodes.EV_KEY:
            if event.value == 1:
                if event.code == SixAxis.ec_select:
                    button = SixAxis.button_select
                elif event.code == SixAxis.ec_start:
                    button = SixAxis.button_start
                elif event.code == SixAxis.ec_left_stick:
                    button = SixAxis.button_left_stick
                elif event.code == SixAxis.ec_right_stick:
                    button = SixAxis.button_right_stick
                elif event.code == SixAxis.ec_d_up:
                    button = SixAxis.button_d_up
                elif event.code == SixAxis.ec_d_down:
                    button = SixAxis.button_d_down
                elif event.code == SixAxis.ec_d_left:
                    button = SixAxis.button_d_left
                elif event.code == SixAxis.ec_d_right:
                    button = SixAxis.button_d_right
                elif event.code == SixAxis.ec_square:
                    button = SixAxis.button_square
                elif event.code == SixAxis.ec_circle:
                    button = SixAxis.button_circle   
                elif event.code == SixAxis.ec_triangle:
                    button = SixAxis.button_triangle
                elif event.code == SixAxis.ec_cross:
                    button = SixAxis.button_cross
                elif event.code == SixAxis.ec_PS:
                    button = SixAxis.button_ps
                elif event.code == SixAxis.ec_l1:
                    button = SixAxis.button_l1
                elif event.code == SixAxis.ec_r1:
                    button = SixAxis.button_r1
                elif event.code == SixAxis.ec_l2:
                    button = SixAxis.button_l2   
                elif event.code == SixAxis.ec_r2:
                    button = SixAxis.button_r2
                else:
                    button = None
                if button is not None:
                    self.button_pressed |= 1 << button
                    for button_handler in self.button_handlers:
                        if button_handler['mask'] & (1 << button) != 0:
                            button_handler['handler'](button)

    class Axis():
        def __init__(self, name, invert=False, dead_zone=0.00, hot_zone=0.00):
            self.name = name
            self.center = 0.5
            self.max = 0.9
            self.min = 0.1
            self.value = 0.5
            self.invert = invert
            self.dead_zone = dead_zone
            self.hot_zone = hot_zone

        def corrected_value(self):
            high_range = self.max - self.center
            high_start = self.center +self.dead_zone * high_range
            high_end = self.max - self.hot_zone * high_range

            low_range = self.center - self.min
            low_start = self.center - self.dead_zone * low_range
            low_end = self.min +self.hot_zone *low_range

            if self.value > high_start:
                if self.value > high_end:
                    result = 1.00
                else:
                   result = (self.value - high_start) / (high_end - high_start)
            elif self.value < low_start:
                if self.value < low_end:
                    result = -1.0
                else:
                    result = (self.value - low_start) / (low_start - low_end)
            else:
                result = 0
            if not self.invert:
                return result
            else:
                return -result
        
        def _set(self, new_value):
            self.value = new_value
            if new_value > self.max:
                self.max = new_value
            elif new_value < self.min:
                self.min = new_value


