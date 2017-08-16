import subprocess
import time

# Message
low = "Battery is Low, Connect Your Charger"

def read():
    # bash syntax 

    # acpi -b => "Battery 0: Charging, 17%, 01:39:53 until charged"
    # acpi -b | cut -d"," -f2 => "17%"
    
    command = 'acpi -b | cut -d"," -f2'
    bat = subprocess.Popen(["/bin/bash", "-c", command], stdout=subprocess.PIPE)
    status=bat.communicate()[0].decode("utf-8")
    return status


while True:
   status=read()

   if int(status.split('%')[0])<20:
       subprocess.Popen(['notify-send',low])

   time.sleep(300) # 300 seconds or 5 min


