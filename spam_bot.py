import pyautogui
import time

message = "This is a spam message!"

repeat = 10

time.sleep(5)

for i in range(repeat):
    pyautogui.typewrite(message)
    
    pyautogui.press("enter")
    
    time.sleep(0.5)
