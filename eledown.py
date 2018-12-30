from time import sleep
import RPi.GPIO as GPIO

DIR =  38  # Direction GPIO Pin
STEP = 40  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation

def elevator_down(SPR):
    # SPR = 7500  # Steps per Revolution (360 / 7.5)
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR, CW)
    GPIO.setwarnings(False)

    step_count = SPR
    delay = .001


    GPIO.output(DIR, CCW)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)

        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)


    GPIO.cleanup()