
import pytesseract
import PIL
import numpy as np
import constants
import glob, os
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
def screenshot():
    screenshot = None
    arq = None
    x = 0
    while len([name for name in os.listdir('.') if os.path.isfile(name)]) < 1 or screenshot is None:
        for arq in glob.glob("*.png"):
            screenshot = PIL.Image.open(arq)
        time.sleep(0.1)
        x = x + 1
        if x == 10:
            return None, None
    
    screenshot = PIL.ImageOps.invert(screenshot.convert('RGB'))
    return screenshot, arq

def monsters(screenshot):
    monsters = screenshot.crop(constants.monsters_area)
    monsters_colors = list(np.array(monsters.getcolors(700))[:,1])
    if constants.attack_color in monsters_colors:
        attacking = True
    else:
        attacking = False
    if constants.monster_color in monsters_colors:
        monster_present = True
    else:
        monster_present = False
    return attacking, monster_present

def health(screenshot):
    low_health = screenshot.crop(constants.low_health_area)
    high_health = screenshot.crop(constants.high_health_area)
    high_health = list(high_health.getdata())
    low_health = list(low_health.getdata())
    health = 0
    if constants.health_color not in low_health:
        health = health + 1
    if constants.health_color not in high_health:
        health = health + 1

    return health

def map(screenshot):
    map_image = screenshot.crop(constants.map_area)
    lista = list(map_image.getdata())
    x = np.reshape(np.array([x in constants.map_walkable for x in lista]), (-1, 105))
    return x

def food(screenshot):
    food_image = screenshot.crop(constants.food_area)
    lista = list(food_image.getdata())
    battle = constants.battle in lista
    food = constants.food in lista
    return food, battle
        
def mana(screenshot):
    low_health = screenshot.crop(constants.low_mana_area)
    high_health = screenshot.crop(constants.high_mana_area)
    high_health = list(high_health.getdata())
    low_health = list(low_health.getdata())
    health = 0
    if constants.mana_color in low_health:
        health = health + 1
    if constants.mana_color in high_health:
        health = health + 1

    return health