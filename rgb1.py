#!/usr/bin/env python
# coding: utf-8

import RPi.GPIO
import time

R, G, B = 14, 15, 18

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(R, RPi.GPIO.OUT)
RPi.GPIO.setup(G, RPi.GPIO.OUT)
RPi.GPIO.setup(B, RPi.GPIO.OUT)

pwmR = RPi.GPIO.PWM(R, 50)
pwmG = RPi.GPIO.PWM(G, 50)
pwmB = RPi.GPIO.PWM(B, 50)

pwmR.start(0)
pwmG.start(0)
pwmB.start(0)

try:
    t = 1
    while True:
        # Dark
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)
        
        # Red light
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)
        
        # Green light
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
        time.sleep(t)
        
        # Blue light
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
        time.sleep(t)

except KeyboardInterrupt:
    pass

pwmR.stop()
pwmG.stop()
pwmB.stop()

RPi.GPIO.cleanup()
