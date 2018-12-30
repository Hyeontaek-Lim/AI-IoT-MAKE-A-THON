import sys                      
from time import sleep
import RPi.GPIO as GPIO

DIR = 38   # Direction GPIO Pin
STEP = 40  # Step GPIO Pin
dDIR = 3
dSTEP = 5
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 1500   # Steps per Revolution (360 / 7.5)#elevator
nSPR = 90


def elevator_up(person_in):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR, CW)

    step_count = SPR
    nstep_count = nSPR
    
    ret = 0

    if(person_in[0] != 0):     #start person_in 
        print("Current person_in is start person_in. \n Error!")
        exit(0) #exception
    else:  
        cnt = person_in.count(1)  #num of stopped
        #for i in range(len(person_in)):
        while cnt != 0:
            for i in range(len(person_in)):
                if person_in[i] == 1:
                    tmp = i+1
                    cnt -= 1

                    for x in range(step_count):
                        GPIO.output(STEP, GPIO.HIGH)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(.001)#speed
                    print("Arrive on " + str(i+1) + "F. Have a nice day")

                    sleep(5)
                    
                    ret += 1500
                    

                    if cnt == 0:
                        print("stop")
                        break
    
                else: #passing person_in
                    print(str(i+1) + "F")
                    sleep(1.5)
        
                if cnt == 0:
                    print("no floor")
                #break
            #time.sleep(1) #Give a few term.
        
    print("Complete.")
    GPIO.cleanup()

    return ret