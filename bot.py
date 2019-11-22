import timeit
code_to_test = """
import pyautogui
import PIL
from pytesseract import image_to_string


print(image_to_string(PIL.Image.open('wagner.png')))
"""
#pyautogui.keyDown("y")

#pyautogui.keyUp("y")

#pyautogui.moveTo(3500,200,duration=0.2)

elapsed_time = timeit.timeit(code_to_test, number=1)/1
print(elapsed_time)
