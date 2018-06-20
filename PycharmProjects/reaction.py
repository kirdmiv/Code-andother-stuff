import pyautogui
import time

while True:
    r, g, b = pyautogui.pixel(450, 333)
    if r == 75 and g == 219 and b == 106:
        pyautogui.click(450, 333)
        break
    time.sleep(0.01)