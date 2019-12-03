
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
d = True
w = 0
c = 0
move_speed = 20
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
    pyautogui.click(x=1000, y = 200)

    pyautogui.keyUp("shift")
    


while True:
    if len([name for name in os.listdir('.') if os.path.isfile(name)]) < 1:
        pyautogui.press("p")
    time.sleep(0.1)

    screenshot, arq = processing.screenshot()
    
    if screenshot is not None:
        attacking, monster_present = processing.monsters(screenshot)
        health = processing.health(screenshot)
        mana = processing.mana(screenshot)
        food, battle = processing.food(screenshot)
        way, down, up = processing.map(screenshot)



        if monster_present:
            if not attacking:
                pyautogui.press("e")
                pyautogui.click(x = 1895, y = 220)
                attacking = True
                loot_around()
            
        
        if c % move_speed == 0:
            if not attacking:
                loot_around()
                if w < 6:
                    x = random.randrange(0, len(way))
                    pos = way[x]
                    w = w + 1
                    pyautogui.click(x = 1895, y = 220)
                else:
                    pos = (0,0)
                    if d and len(down) > 0:
                        x = random.randrange(0, len(down))
                        pos = down[x]
                        pyautogui.click(x = 1895, y = 195)
                    elif d and len(down) == 0:
                        d = False
                        w = 0
                        move_speed = 20
                    elif not d and len(up) > 0:
                        x = random.randrange(0, len(up))
                        pos = up[x]
                        pyautogui.press("u")
                        pyautogui.click(button="left", x = 960, y = 540-offset)
                        move_speed = 5
                    elif not d and len(up) == 0:
                        d = True
                        w = 0
                        move_speed = 20
                        pyautogui.click(x = 1895, y = 195)
                pyautogui.click(x = 1710 + int(pos[1] * 1.26), y = 35 + int(pos[0]* 1.24))

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
        try:
            os.remove(arq)
        except:
            print("bugou")
    else:
        pass



#pyautogui.keyDown("y")

#pyautogui.keyUp("y")

#pyautogui.moveTo(3500,200,duration=0.2)
