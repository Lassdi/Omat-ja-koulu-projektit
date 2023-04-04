import hid
#import RPi.GPIO as GPIO
from time import sleep
import threading

class reader(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.result = 0
        self.data = None
        self.buttons = [
            (17, 8), 
            (17, 4),
            (17, 16), 
            (16, 4), 
            (16, 31), 
            (16, 2),
            (16, 47), 
            (16, 6), 
            (19, 2), 
            (18, 128),
            (19, 4),
            (16, 0), 
            (17, 1), 
            (16, 79),  
            (17, 64),  
            (17, 32),  
            (17, 2),  
            (16, 143), 
            (18, 4), 
            (18, 2), 
            (18, 64), 
            (18, 32),
            (18, 16), 
            (18, 8),
            (18, 1), 
            (17, 128), 
            ]
    
    def run(self):
        
        devices = hid.enumerate()
        device_info = next((d for d in devices if d['vendor_id'] == 1047 and d['product_id'] == 324), None)

        if device_info is None:
            print('Device not found')
            exit()

        device = hid.device()
        device.open_path(device_info['path'])
        self.data = []
       
        while True:
            data = device.read(64)
            button_matched = False 

            for button in self.buttons:
                index = button[0]
                value = button[1]

                if data[index] == value:
                    self.result = self.buttons.index(button)+1
                    button_matched = True
                    break

            if not button_matched:
                self.result = 0  

    def get(self):
        return self.result
        


        


# buttons = [
#     (17, 8), 
#     (17, 4),
#     (17, 16), 
#     (16, 4), 
#     (16, 31), 
#     (16, 2),
#     (16, 47), 
#     (16, 6), 
#     (19, 2), 
#     (18, 128),
#     (19, 4),
#     (16, 0), 
#     (17, 1), 
#     (16, 79),  
#     (17, 64),  
#     (17, 32),  
#     (17, 2),  
#     (16, 143), 
#     (18, 4), 
#     (18, 2), 
#     (18, 64), 
#     (18, 32),
#     (18, 16), 
#     (18, 8),
#     (18, 1), 
#     (17, 128), 
# ]

# def read_data(data, buttons):
#     result = 0
#     for button in buttons:
#         index = button[0]
#         value = button[1]
#         if data[index] == value:
#             result = buttons.index(button)+1
#             break
#     print(result)


# # Set up the GPIO pins for the servo
# # GPIO.setmode(GPIO.BOARD)
# # GPIO.setup(11, GPIO.OUT)
# # servo = GPIO.PWM(11, 50)
# # servo.start(0)

# devices = hid.enumerate()

# device_info = next((d for d in devices if d['vendor_id'] == 1047 and d['product_id'] == 324), None)

# if device_info is None:
#     print('Device not found')
#     exit()


# device = hid.device()
# device.open_path(device_info['path'])
# # Read data from the HID device and convert it to a servo position
# # while True:
# #     data = device.read(64) # read 8 bytes of data
# #     if data:
        
# #         handle1 = data[0]
# #         handle2 = data[1] * 2
# #         position1 = (handle1 / 255.0) * 180.0
# #         position2 = (handle2 / 255.0) * 180.0
# #         position = (position1 + position2) / 2.0 # take the average of the two positions
# #         servo.ChangeDutyCycle(position / 18.0 + 2.5) # convert position to duty cycle
# #                                                     # see note below about duty cycle
# while True:
#     data = device.read(64)
#     #print(data)
#     read_data(data, buttons)
#     #DATA


 
# # Clean up
# #servo.stop()
# #GPIO.cleanup()