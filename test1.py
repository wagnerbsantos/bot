
import pyautogui
import PIL
import pytesseract
import time
import glob, os
import numpy as np
import constants

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
pasta = "C:\\Users\\wag09\\AppData\\Local\\Tibia\\packages\\Tibia\\screenshots"

os.chdir(pasta)

pyautogui.press("p")
screenshot = None
time.sleep(2)
c = 0
while (screenshot is None):
    for arq in glob.glob("2*.png"):
        screenshot = PIL.Image.open(arq)
    time.sleep(0.1)
    screenshot.save("new.png")
    c = c+1
print(c)
