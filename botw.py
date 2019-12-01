
import pyautogui
import PIL
import time
import glob, os
import numpy as np
import constants
import random
import processing


attacking = False
monster_present = True
walking = False
offset = 100
x_center = 960
y_center = 540-offset
w = 0
c = 0
os.chdir(constants.screenshot_folder)
for arq in glob.glob("*.png"):
    os.remove(arq)
    print(arq) 
pyautogui.click(x=1000, y = 10)
time.sleep(1)


def loot_around():
    pyautogui.keyDown("shift")
    pyautogui.click(button="right", x = 960, y = 540-offset)
    pyautogui.click(button="right", x = 920, y = 540-offset)
    pyautogui.click(button="right", x = 1050, y = 540-offset)
    pyautogui.click(button="right", x = 960, y = 620-offset)
    pyautogui.click(button="right", x = 920, y = 620-offset)
    pyautogui.click(button="right", x = 1050, y = 620-offset)
    pyautogui.click(button="right", x = 960, y = 500-offset)
    pyautogui.click(button="right", x = 920, y = 500-offset)
    pyautogui.click(button="right", x = 1050, y = 500-offset)

    pyautogui.keyUp("shift")
    


while True:
    pyautogui.press("p")

    screenshot, arq = processing.screenshot()
    
    if screenshot is not None:
        attacking, monster_present = processing.monsters(screenshot)
        health = processing.health(screenshot)
        mana = processing.mana(screenshot)
        food, battle = processing.food(screenshot)
        mapa = processing.map(screenshot)


        if monster_present:
            if not attacking:
                pyautogui.press("e")
                pyautogui.click(x = 1895, y = 220)
                attacking = True
                loot_around()
            
        
        if c % 6 == 0:
            if not attacking:
                loot_around()
                found = False
                while not found:
                    x_target = random.randrange(0, mapa.shape[0])
                    y_target = random.randrange(0, mapa.shape[1])
                    if mapa[x_target, y_target]:
                        found = True
                        pyautogui.click(x = 1710 + int(y_target * 1.26), y = 35 + int(x_target* 1.24))
                        pyautogui.click(x = 1895, y = 220)
        print(health, mana)

        if mana == 2:
            pyautogui.press("f3")
        if health == 1 and mana == 0:
            pyautogui.press("f4")
        if health == 1:
            pyautogui.press("f3")
        
        
        if health == 0:
            pyautogui.press("f2")
        if food and (health == 1 or mana == 1):
            pyautogui.press("f5")
            pyautogui.press("f8")
        c = c+1
        screenshot.close()
        os.remove(arq)
    else:
        pass



#pyautogui.keyDown("y")

#pyautogui.keyUp("y")

#pyautogui.moveTo(3500,200,duration=0.2)
