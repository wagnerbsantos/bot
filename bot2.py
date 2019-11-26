
import pyautogui
import PIL
import pytesseract
import time
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
#while True:
screenshot = pyautogui.screenshot("file.png")
monsters_area = (10, 30,200, 200)
monsters = screenshot.crop(monsters_area)
monsters.save("monsters.png")
print("monsters:", pytesseract.image_to_string(monsters))

health_area = (500, 30,700, 50)
health = screenshot.crop(health_area)
health.save("health.png")
print("health:", pytesseract.image_to_string(health))

mana_area = (1250, 30,1450, 50)
mana = screenshot.crop(mana_area)
mana.save("mana.png")
print("mana:", pytesseract.image_to_string(mana))
#time.sleep(5)

#pyautogui.keyDown("y")

#pyautogui.keyUp("y")

#pyautogui.moveTo(3500,200,duration=0.2)

#print(pytesseract.image_to_string(PIL.Image.open('cami.png')))

#pyautogui.keyDown("y")

#pyautogui.keyUp("y")

#pyautogui.moveTo(3500,200,duration=0.2)
