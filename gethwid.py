import datetime
import socket
import subprocess
import os
import ctypes

# Import
date_time = datetime.datetime.now()
pc = socket.gethostname()
ip = socket.gethostbyname(pc)
creator = "Mailar#0001"
sub = "This is my first public python script what helps you finding PC information !"
sub2 = "You can run this on vs code or python idle !"

# Color
os.system('color 1f') # sets the background to blue

# Title
ctypes.windll.kernel32.SetConsoleTitleA("Mailar's HWID PRINTER")

# Hwid
def HWID():
   cmd = 'wmic csproduct get uuid'
   uuid = str(subprocess.check_output(cmd))
   pos1 = uuid.find("\\n")+2
   uuid = uuid[pos1:-15]
   return uuid

# Code
print(
"\nGet PC HWID",
"\nDeveloped by: "+creator,
"\nSub Message: "+sub,
"\nSub Message 2: "+sub2,
"\n",
"\nOpen Source:",True,
"\nPC: "+pc,
"\nIP: "+ip,
"\nHWID: "+HWID())

os.system("pause")