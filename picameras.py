"""
### distance-aware security recording
### author : Hyuntaek Lim
### created : 2018-12-22
"""

import RPi.GPIO as GPIO
import time
import picamera

def startRecord():
    now = time.localtime()
    name = str(now.tm_year) + str(now.tm_mday) + str(now.tm_hour) + str(now.tm_min) + str(now.tm_sec)
    video = '/home/pi/' + name + '.h264'

    with picamera.PiCamera() as camera:                
        #Video recording start
        camera.start_preview()
        camera.start_recording(video)
        time.sleep(5)
        camera.stop_recording()
        camera.stop_preview                
        
    GPIO.cleanup() 

