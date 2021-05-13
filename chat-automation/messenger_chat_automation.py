# pip install pyautogui

import pyautogui
import time

text = 'I need to code now!'

counter = 3
while counter > 0 :
    time.sleep(3)
    pyautogui.typewrite(data)
    pyautogui.press('enter')
    counter -= 1
