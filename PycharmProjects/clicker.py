import pyautogui
import time
import keyboard

while True:
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        print('You Pressed A Key!')
        break  # finishing the loop
    pyautogui.click(619, 493)
    time.sleep(0.15)
    r, g, b = pyautogui.pixel(1016, 526)
    if r > 150:
        pyautogui.click(1016, 526)