from os import popen
from shutil import copy2, rmtree
from sys import exit
from subprocess import Popen

print("Reloader as started")

copy2("PythonAutoUpdate\\LatestBuild\\mainscript.py", "PythonAutoUpdate")

Popen("C:/Users/Striz/AppData/Local/Programs/Python/Python38/python.exe PythonAutoUpdate\\main.py", shell=True)

exit("Exiting to restart the main program")