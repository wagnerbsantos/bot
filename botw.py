
import pyautogui
import PIL
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


print(pytesseract.image_to_string(PIL.Image.open('cami.png')))

#pyautogui.keyDown("y")

#pyautogui.keyUp("y")

#pyautogui.moveTo(3500,200,duration=0.2)
