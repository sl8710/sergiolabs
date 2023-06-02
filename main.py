import time
from RoomController import *
time.sleep(0.1) # Wait for USB to become ready
print("Hello, Pi Pico!")
myroom = RoomController()
myroom.run()
