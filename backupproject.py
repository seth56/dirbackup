import shutil
from datetime import datetime
import time
import os

colors = "\u001b["
reset = colors + "0m"
cyan = colors + "36m"
magenta = colors + "35m"
bg_cyan = colors + "46m"
bg_magenta = colors + "45m"
bold = colors + "1m"

print("\n" + bg_cyan + magenta + "*****************************************")
print(bold + black +             "          WELCOME TO BACKUP.PY!          ")
print(magenta +                  "*****************************************" + reset + "\n")

src = input(cyan + "Enter source to copy: " + reset)
while src == "":
    src = input(cyan + "Enter source to copy: " + reset)

rootdir = '/home/seth/Documents/Backups/'
print("\n" + magenta + "FOLDERS IN CURRENT DIRECTORY" + reset)
for file in os.listdir(rootdir):
        if "." not in file:
            print("   ~ " + file)

dest = input("\n" + cyan + "Enter destination: " + reset)
while dest == "":
    dest = input(cyan + "Enter destination: " + reset)
minutes = input(cyan + "Enter the minutes in between each backup: " + reset)
while minutes == "":
    minutes = input(cyan + "Enter the minutes in between each backup: " + reset)

print("\nRunning every " + str(minutes) + " minutes.")

while True:
    now = datetime.now()
    dt_string = str(now.strftime("%d-%m-%Y_%H:%M:%S"))
    shutil.copytree(src, dest + "/" + dt_string)
    print(dest + "/" + dt_string + magenta + " CREATED" + reset)
    time.sleep(int(minutes)*60)
