import timeit
import pyautogui

from pytesseract import image_to_string

def foo():
    return screenshot

code_to_test = """
import PIL
import pyautogui
from pytesseract import image_to_string
screenshot = pyautogui.screenshot("file.png")
area1 = (40, 10,90, 25)
part1 = screenshot.crop(area1)

print(image_to_string(part1))


print(screenshot)
area2 = (500, 500,550, 550)

part2 = screenshot.crop(area2)
part2.save("part2.png")
print(image_to_string(part2))
"""
elapsed_time = timeit.timeit(code_to_test, number=1)/1
print(elapsed_time)


#screenshot = pyautogui.screenshot("file.png", region =(40, 10,50, 15) )
#screenshot.show()
