from subprocess import Popen
import subprocess
import mainscript
import requests
from os import getcwd
import time

starttime = time.time()

interval = 1

label = subprocess.check_output(["git", "describe"]).strip()

print(label)

while True:
    mainscript.test()

    counter = 10
    while counter != 0:
        print(counter)
        time.sleep(interval - ((time.time() - starttime) % interval))
        counter -= 1
        
    Popen("C:/Users/Striz/AppData/Local/Programs/Python/Python38/python.exe PythonAutoUpdate\\reloader.py", shell=True) # start reloader

    exit("Exiting and updating files...")

