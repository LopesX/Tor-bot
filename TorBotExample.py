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
    #c = os.startfile("Your  Path to Tor ")
c = os.startfile("C:/Users/User/Desktop/Tor Browser/Browser/firefox.exe")
    #os.system("taskkill /f /im  explorer.exe")



        
while True:
#wait time to initialize network
    time.sleep(20)

#Tor´s webbar adress cordinates x,y
    pyautogui.moveTo(1100, 75)

    pyautogui.click()

#Type web adress

    pyautogui.typewrite('www.youtube.com', interval=0.25)

    pyautogui.hotkey('enter')

    time.sleep(5)

#Type youtube video search
    pyautogui.moveTo(1100, 130)
    pyautogui.click()
    pyautogui.typewrite('lovetheoryrecords', interval=0.25)
    pyautogui.hotkey('enter')
    time.sleep(5)


    pyautogui.moveTo(900, 900)
    pyautogui.click()

    time.sleep(playtime)

#Add 1 to number of loops
    control = control + 1
    time.sleep(5)

#request new ip 
    pyautogui.hotkey('ctrl', 'shift', 'u')
#use this instead of line above if NOT USING Tor, this is a chrome example ,
    #change 'chrome.exe' to your browser exe file)
     
    #os.system("taskkill /f /im  chrome.exe")


#print loop number
    print('Loop nº', control)


    if control == NumOfLoops:
        os.system("taskkill /f /im  firefox.exe")
        print(control, 'number of loops done')
        break
    





