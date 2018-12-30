import subprocess

mystring = subprocess.check_output(["sudo", "iwlist", "wlan0", "scan"], universal_newlines=True)

word = 'ESSID:"KTW"'
mac_idx = mystring.index(word)
startidx = mystring[:mac_idx].index("Address") + 9

print(mystring[startidx:mac_idx])