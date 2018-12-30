"""
### Protect
### author : Hyuntaek Lim
### created : 2018-12-22
"""

#-----------------------------------
# Firebase Connect Part
#-----------------------------------
from firebase import firebase
firebase = firebase.FirebaseApplication("https://devsign-2018.firebaseio.com/", None)

# import std lib
import os
import subprocess
import time

# import my lib
import cache
import picameras



run = True
while run:
    #-----------------------------------
    # I turn on the Wi-Fi power again and wait for 3 seconds to stop the program.
    # Due to wifi connection delay
    #-----------------------------------
    comp = firebase.get('/Hotspot', 'stat')
    print str(comp) + '\n'+'\n'
    if(str(comp) == 'connect'):

        # record
        picameras.startRecord()

        #--------------------------------------------
        # Login info
        #--------------------------------------------
        curLoginID = firebase.get('/login', 'id')
        curLoginPW = firebase.get('/login', 'pw')
        curLoginWIFI = firebase.get('/login', 'wifi')
        

        
        if cache.search(curLoginID, curLoginPW, curLoginWIFI):
            firebase.put('/Hotspot', 'stat', "User vertification complete!")

            import po
            up_data = po.elevator_up([0,1,1,1,1])

            import eledown
            eledown.elevator_down(up_data)
