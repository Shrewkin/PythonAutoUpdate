import time
import urllib.request
import logging
from subprocess import Popen
import Bot
import os


######################## Github Implementation
def GithubDownload():
    botURL = "https://raw.githubusercontent.com/Shrewkin/Fonzie-Bot/main/Code/Bot.py"
    logging.info("INFO: File Download has started...")
    filename, headers = urllib.request.urlretrieve(botURL, filename="Bot.py")
    logging.warning("INFO: Download Complete")
    logging.warning("DEBUG: Downloaded Bot.py into directory: ", filename)
    logging.warning("DEBUG: Downloaded Headers: \n", headers)

########################### AutoUpdater
def UpdateLoop():
    starttime = time.time()
    interval = 1

    # Update Loop
    while True:
        # Runs the script
        Bot.test()

        # Number of seconds in a day
        #counter = 86400
        counter = 5
        while counter != 0:
            time.sleep(interval - ((time.time() - starttime) % interval))
            counter -= 1
        
        GithubDownload()
        
        Popen("python3 reloader.py", shell=True) # start reloader

        exit("Exiting and updating files...")
    
UpdateLoop()