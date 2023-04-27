import os
import time

os.system('/karotz/bin/led -l FF0000')

#Tourelle active
os.system('/usr/karotz/FreeRabbits/PlaySound Turret_active.mp3')
os.system('/karotz/bin/ears &') # Oreilles leves vers le haut (reset)
os.system('/karotz/bin/led -l FF0000 &') # LED rouge, aussi dispo /karotz/bin/led -l 00FFFF -p 000000 -d 700

time.sleep(2)
os.system('/usr/karotz/FreeRabbits/PlaySound Turret_scan.mp3')

#Tourelle attente
time.sleep(5)

#Tourelle tir
os.system('/karotz/bin/ears 2 50 2 50 &') # Oreilles en position de tir
os.system('/usr/karotz/FreeRabbits/PlaySound Turret_deploy.mp3')
os.system('/usr/karotz/FreeRabbits/PlaySound Turret_hello.mp3')
time.sleep(1)
os.system('/usr/karotz/FreeRabbits/PlaySound Turret_fire.mp3 &')

i=0
while i<=21:
    time.sleep(0.05)
    os.system('/karotz/bin/led -l 000000 &') # LED eteint
    time.sleep(0.05)
    os.system('/karotz/bin/led -l FF0000 &') # LED rouge
    i+=1
time.sleep(0.2)
time.sleep(1)

#Tourelle rangee
os.system('/karotz/bin/ears 0 50 0 50')
os.system('/usr/karotz/FreeRabbits/PlaySound Turret_retract.mp3')

time.sleep(2)

os.system("/karotz/bin/led -l 000000")

#Audio(url="https://i1.theportalwiki.net/img/7/77/Turret_turret_active_5.wav")