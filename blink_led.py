import pyfirmata
import time

usb_port = '/dev/cu.usbmodem14101'

print("conecting to board...")
board = pyfirmata.Arduino(usb_port)
print("done")

flag = 0
print("Loop start")
while True:
   board.digital[13].write(flag)
   time.sleep(0.1)
   if flag:
      flag = 0
   else:
      flag = 1
