import sys
from time import sleep
import RPi.GPIO as GPIO

DIR = 14
STEP = 15
CW = 1
CCW = 0
SPR = 1200

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = .00001

person_in = [0, 1, 1, 0, 1]
# person_in = [int(x) for x in input ('which floor will the person coming in?').split()]
if(person_in[0] != 0):
    print("Current floor is start floor. \n Error!!")
    exit(0)

cnt = person_in.count(1)
for i in range(len(person_in)):
    if(person_in[i] == 1):
        tmp = i + 1
        print("Arrive on " + str(tmp) + "F. ^^")
        cnt -= 1

        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(0.0001)

            if 1 not in person_in[tmp:]:
                print("stop!")
                break

    else:
        print(str(i+1) + "F")
        sleep(0.5)
        if 1 not in person_in[i+1:]:
            print("stop!")
            break

print("Complete.")