import sys                      
from time import sleep
import RPi.GPIO as GPIO

DIR =  38  # Direction GPIO Pin
STEP = 40  # Step GPIO Pin
dDIR = 2
dSTEP = 3
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 2400   # Steps per Revolution (360 / 7.5)#elevator
nSPR = 90

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR


person_in = [0, 1, 0, 1, 0] # 1~5 person_in

    #person_in = [int(x) for x in input('which person_in will the person coming in?').split()]
if(person_in[0] != 0):     #start person_in 
    print("Current person_in is start person_in. \n Error!")
    exit(0) #exception
else:  
    cnt = person_in.count(1)  #num of stopped
        #for i in range(len(person_in)):
    if cnt != 0:
        for i in range(len(person_in)):
            if person_in[i] == 1:
                tmp = i + 1
                cnt -= 1
                    
                for x in range(step_count):
                    GPIO.output(STEP, GPIO.HIGH)
                    GPIO.output(STEP, GPIO.LOW)
                    sleep(.001)#speed
                print("Arrive on " +str(i+1) + "F. Have a nice day")
                    
                sleep(5)
      
                if cnt == 0:
                    print("stop")
                    break
            else: #passing person_in
                print(str(i+1) + "F")
                sleep(1.5)
                    
            if cnt == 0:
                print("no floor")
           #break
        #if cnt == 0:
          #  print("stop")
           # exit(0)
                #break
            #time.sleep(1) #Give a few term.
            
print("Complete.")
GPIO.cleanup()
    