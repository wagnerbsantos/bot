import numpy as np
import cv2
from mss.linux import MSS as mss
from PIL import Image
import time
import pyautogui as pg
import mss
import numpy
import pyautogui

pyautogui.FAILSAFE = False


def process_image(original_image):

    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    processed_image = cv2.Canny(
        processed_image, threshold1=200, threshold2=300)
    return processed_image


def throw(position):
    pyautogui.moveTo(position)
    pyautogui.mouseDown()
    time.sleep(0.5)
    pyautogui.mouseUp()


def usebait(x, y, lastposition):
    pyautogui.moveTo(x, y)
    pyautogui.rightClick()
    pyautogui.press("=")
    pyautogui.moveTo(lastposition)


def ss():

    op = 1
    with mss.mss() as sct:
        monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}

    last_time = time.time()
    count = 0
    fish = False
    media = 0
    n = 0
    c = 0
    time.sleep(2)
    fishpos = pyautogui.position()
    inv1y = 550
    inv1x = 1600
    nofish = 0
    toeat = True
    hooked = False
    while True:
        img = numpy.array(sct.grab(monitor))
        # cv2.imshow("OpenCV/Numpy normal", img)
        im = Image.fromarray(img)
        pix = (im.load())
        find = 0
        for pos in range(800, 1100):
            if pix[pos, 560] == (100, 115, 129, 255):
                find = pos
                break
            if pix[pos, 559] == (21, 90, 52, 255):
                find = pos
                break
            if pix[pos, 561] == (100, 115, 129, 255):
                find = pos
                break
            if pix[pos, 562] == (100, 115, 129, 255):
                find = pos
                break
            if pix[pos, 558] == (100, 115, 129, 255):
                find = pos
                break
        # print(find)
        if find != 0:
            c = c + 1
            if c >= 7 and find > 910:
                pyautogui.mouseUp()
                c = 0
            if c >= 5 and find > 960:
                pyautogui.mouseUp()
                c = 0
            fish = False
            if find < 1010:
                pyautogui.mouseDown()
                mouse = True
            else:
                pyautogui.mouseUp()
        elif hooked:
            pyautogui.mouseDown()
            count = 0
            fish = False
            hooked = False
        else:
            if fish:
                p = pyautogui.position()
                area = (p[0]-25, p[1]-25, p[0]+25, p[1]+10)
                hook = numpy.array(im.crop(area))
                processed_image = process_image(hook)
                mean = np.mean(processed_image)
                #cv2.imshow("OpenCV/Numpy normal", processed_image)
                media = (media+mean)/2
                #print('mean =', mean)
                if mean == float(0.0):
                    fish = False
                if mean < media*0.8:
                    print('SSSSSSSS')
                    pyautogui.click(button='left')
                    hooked = True
                    nofish = nofish + 1
                    if nofish >= 11:
                        toeat = True
                        nofish = 0
                    media = 0
                    fish = False
                    if mean < 0.2:
                        pyautogui.click(button='left')
                    continue
            else:
               # time.sleep(5)
                if count == 5:
                    count = 0
                    if not fish:
                        if toeat:
                            usebait(inv1x, inv1y, fishpos)
                            time.sleep(2)
                            toeat = False
                        fishpos = pyautogui.position()
                        throw(fishpos)
                        time.sleep(2)
                    fish = True
                count = count + 1
        key = cv2.waitKey(70)


time.sleep(2)
ss()
