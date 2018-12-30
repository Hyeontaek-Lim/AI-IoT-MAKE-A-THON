import sys                      
from time import sleep
import RPi.GPIO as GPIO

DIR = 14   # Direction GPIO Pin
STEP = 15  # Step GPIO Pin
dDIR = 2
dSTEP = 3
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 8000   # Steps per Revolution (360 / 7.5)#elevator
nSPR = 90

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR

def elevator_up(person_in):
    ret_SPR = 0
    # person_in = [0, 1, 0, 0, 0] # 1~5 person_in

    if(person_in[0] != 0):     #start person_in 
        print("Current person_in is start person_in. \n Error!")
        exit(0) #exception
    else:  
        cnt = person_in.count(1)  #num of stopped
        #for i in range(len(person_in)):
        while cnt != 0:
            for i in range(len(person_in)):
                if 1 in person_in: #stopped
                    tmp = person_in.index(1) + 1
                    cnt -= 1
                    print("Arrive on " +str(tmp) + "F. Have a nice day")
                
                    for x in range(step_count):
                        GPIO.output(STEP, GPIO.HIGH)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(.0001)#speed

                    sleep(3)
                    SPR += 1600*tmp
                
            
        if cnt == 0:
            print("no floor")
        #break
    
        else: #passing person_in
            print(str(i+1) + "F")
            sleep(.001)
        
            if 1 not in person_in[i+1:]:
                print("stop")
                #break
            #time.sleep(1) #Give a few term.
        
    print("Complete.")
    
    return ret_SPR
