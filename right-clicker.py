
import pyautogui

from pynput import keyboard 

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.KeyCode.from_char('v'):
        pyautogui.mouseDown(button='right')
    elif key == keyboard.KeyCode.from_char('c'):
        pyautogui.mouseUp(button='right')
    elif key == keyboard.Key.esc:
        listener.stop()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


