import os
import time

os.system('/karotz/bin/led -l 000000 &')
time.sleep(5)

os.system('/karotz/bin/led -l 0009ff -p 2b36ff -d 2 &') # Clignote bleu x2 | Usage: /karotz/bin/led -l <primary color> [-p <secondary color>] [-b <secondary color>] [ -d <periodicity> ]

#Copland os enterprise demarrage
#os.system('wget 127.0.0.1/cgi-bin/ears_reset -O /dev/null &') # Oreilles leves vers le haut
os.system('/karotz/bin/ears &')
os.system('wget 127.0.0.1/cgi-bin/sound?id=SEL_Start -O /dev/null &')

time.sleep(10)
#os.system('wget 127.0.0.1/cgi-bin/ears?noreset=1&right=13&left=6 -O /dev/null &')
os.system('/karotz/bin/ears 2 100 15 200 &')
os.system('ps aux | grep /karotz/bin/led | grep -v "grep /karotz/bin/led" | awk \'{print $1}\' | xargs kill -9') # Tue les LEDs
os.system('/karotz/bin/led -l 000552 -p 000000 -d 150 &')
os.system('wget 127.0.0.1/cgi-bin/sound?id=SEL_Wired -O /dev/null &')

#Tourelle attente
time.sleep(5)
#os.system("/karotz/bin/led -l 000000 &")

os.system('ps aux | grep /karotz/bin/led | grep -v "grep /karotz/bin/led" | awk \'{print $1}\' | xargs kill -9') # Tue les LEDs

#i=0
#time.sleep(1)
#while i<=21:
#    time.sleep(0.05)
#    os.system('/karotz/bin/led -l 000000 &') # LED eteint
#    time.sleep(0.05)
#    os.system('/karotz/bin/led -l FF0000 &') # LED rouge
#    i+=1
#time.sleep(0.2)
#time.sleep(1)

#Audio(url="https://i1.theportalwiki.net/img/7/77/Turret_turret_active_5.wav")