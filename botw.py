
import pyautogui
import PIL
import pytesseract
import time
import glob, os
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
pasta = "C:\\Users\\wag09\\AppData\\Local\\Tibia\\packages\\Tibia\\screenshots"
attacking = False
c = 1

def loot_around():
    pyautogui.keyDown("shift")
    offset = 100
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
    c = c+1
    time.sleep(1)
    os.chdir(pasta)
    screenshot = None
    pyautogui.press("p")
    time.sleep(1)
    for arq in glob.glob("2*.png"):
        screenshot = PIL.Image.open(arq)
    if screenshot is not None:
        #screenshot = pyautogui.screenshot("file.png")
        monsters_area = (20, 13,150, 150)
        monsters = screenshot.crop(monsters_area)
        monsters = PIL.ImageOps.invert(monsters.convert('RGB'))
        monsters.save("monsters.png")
        monsterlist = pytesseract.image_to_string(monsters)

        health_image_area = (1480, 278,1534, 293)
        health_image = screenshot.crop(health_image_area)
        health_image = PIL.ImageOps.invert(health_image.convert('RGB'))
        health_image.save("health_image.png")
        health = pytesseract.image_to_string(health_image)
        print(health)
        if not health.isdigit():
            health = 0
        else:
            health = int(health)

        mana_image_area = (1480, 293,1534, 308)
        mana_image = screenshot.crop(mana_image_area)
        mana_image = PIL.ImageOps.invert(mana_image.convert('RGB'))
        mana_image.save("mana_image.png")
        mana = pytesseract.image_to_string(mana_image)
        print(mana)
        if not mana.isdigit():
            mana = 0
        else:
            mana = int(mana)

        num = 0
        monsterlist2 = []
        for monster in monsterlist:
            if monster == "":
                continue
            else:
                monsterlist2.append(monster)
                num = num + 1
                if attacking:
                    attacking = False
                else:
                    attacking = True
        print(c)
        if c >= 2:
            loot_around()
            pyautogui.press("e")
            pyautogui.press("f5")
            pyautogui.press("f8")
            if health < 100 and mana < 10:
                pyautogui.press("f4")
            c = 0
        if health < 150:
            pyautogui.press("f3")
        
        print(health, mana, monsterlist2)
        screenshot.close()
        os.remove(arq)
    else:
        #break
        pass



#pyautogui.keyDown("y")

#pyautogui.keyUp("y")

#pyautogui.moveTo(3500,200,duration=0.2)
