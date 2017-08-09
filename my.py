#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from firebase import firebase 

lightpin   = 7

firebase = firebase.FirebaseApplication('https://testinghaha-f3c61.firebaseio.com',None)

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(lightpin, GPIO.OUT)     # Set Green Led Pin mode to output

def Led(x):
  if x == 0:
    GPIO.output(lightpin, 0)
  if x == 1:
    GPIO.output(lightpin, 1)
 

def loop():
  state = 0
  while True:
    result = firebase.get('/devices', None)
    if (result['rpi']):
      GPIO.output(lightpin, 1)
    else :
      GPIO.output(lightpin, 0)


def destroy():
  GPIO.output(lightpin, GPIO.HIGH)       # Green led off
  GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
      destroy()