import pyautogui
import time
import os
import subprocess

#desired amount of loops
playtime = 30
NumOfLoops = 2
control = 0

pyautogui.FAILSAFE = True

#Clean desktop (Windows)

pyautogui.click(1919,1079)
pyautogui.click()
print('clean desktop')
time.sleep(5)

c = os.startfile("C:/"#Your  Path to Tor "/Tor Browser/Browser/firefox.exe")
  
       
while True:
#wait time to initialize network
    time.sleep(20)

#Edit Tor´s webbar adress cordinates x,y to your screen
    pyautogui.moveTo(1100, 75)

    pyautogui.click()

#Type web adress
                        #enter desired web adress, in this example youtube
    pyautogui.typewrite('www.youtube.com', interval=0.25)

    pyautogui.hotkey('enter')

    time.sleep(5)

#Type youtube video search
    #adgust coordinates to your searchbar  needs x,y             
    pyautogui.moveTo(1100, 130)
    pyautogui.click()
   
    #type whatever you want to look for in search bar
    pyautogui.typewrite('lovetheoryrecords', interval=0.25)
    
    pyautogui.hotkey('enter')
    time.sleep(5)


    pyautogui.moveTo(900, 900)
    pyautogui.click()

    time.sleep(playtime)

#Add 1 to number of loops
    control = control + 1
    time.sleep(5)

#request new identtity on the Tor network 
    pyautogui.hotkey('ctrl', 'shift', 'u')

     
    


#print loop number
    print('Loop nº', control)


    if control == NumOfLoops:
        os.system("taskkill /f /im  firefox.exe")
        print(control, 'number of loops done')
        break
    





