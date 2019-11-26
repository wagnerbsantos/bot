
import pyautogui
import PIL
import pytesseract
import time
from PIL import ImageMath
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

image = PIL.Image.open("part1.png")
#inverted = ImageMath.eval('255-(a)',a=image)
inverted = PIL.ImageOps.invert(image.convert('RGB'))
inverted.save("inverted.png")
print(pytesseract.image_to_string(inverted.crop((0,0,170, 20))))