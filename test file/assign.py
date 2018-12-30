## --------------------------------------------------
## Author : Hyuntaek
## purpose : Implement distance-aware security system
## --------------------------------------------------

import RPi.GPIO as GPIO
import time
import picamera

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Ultrasonic sensor
trig = 16
echo = 18

# Led
led = 22

# Step motor
control_pins = [32, 36, 38, 40]
for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

## Step motor step    
halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
    ]

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

def GetDistance():
    GPIO.output(trig, False)
    time.sleep(0.5)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == False:
        pulse_start = time.time()
        
    while GPIO.input(echo) == True:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)

    return distance

def MotorControl():
    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)

while True:
    ## Continue to show distance information
    print("Distance : ", GetDistance(), "cm")

    try:
        GPIO.output(led, False) # LED OFF(Default)

        if(GetDistance() < 50): # If the distance is shorter than 50
            with picamera.PiCamera() as camera:
                
                #Video recording start
                camera.start_preview()
                GPIO.output(led, True) # LED ON
                camera.start_recording('/home/pi/test.h264') 

                # Store video up to the moment when the distance exceeds 50
                while(GetDistance() < 50):
                    MotorControl() # The motor keeps spinning.
                
                # If the distance is over 50
                camera.stop_recording() # Recording stop
                GPIO.output(led, False) # LED OFF
                camera.stop_preview()
        
    except:
        GPIO.cleanup()
