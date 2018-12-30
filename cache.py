"""
### Database File I/O
### author : Hyuntaek Lim
### created : 2018-12-22
"""

import subprocess

#---------------------------------------------
# new join register
#---------------------------------------------
def newJoin(id, pw, wifi):
    f = open("db.txt", 'a')
    info = id + " " + pw + " " + wifi + "\n"
    f.write(info)

#---------------------------------------------
# Member searching
# exist : return True
# not exist : return -1
#---------------------------------------------
def search(id, pw, wifi):
    search_info = id + " " + pw + " " + wifi + " "

    mystring = subprocess.check_output(["sudo", "iwlist", "wlan0", "scan"], universal_newlines=True)
    word = "ESSID:" + '"' + wifi + '"'
    mac_idx = mystring.index(word)
    startidx = mystring[:mac_idx].index("Address") + 9

    mac_addr =mystring[startidx:mac_idx]
    search_info += mac_addr

    f = open("db.txt", 'r')
    while True:
        cache = ""
        line = f.readline()
        if not line: 
            break
        cache += line
    
    if search_info in cache:
        return True

    return -1