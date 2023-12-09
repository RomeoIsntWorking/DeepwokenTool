import pyautogui
from PIL import Image
import time
import keyboard
import mouse
import autoit


# This clicks the exit button and waits for a bit
def ClickDoor():
    x, y = pyautogui.locateCenterOnScreen("door.png", confidence=0.7)
    autoit.mouse_move(x, y, speed=2)
    autoit.mouse_click("left")
    ClickYes()



def ClickYes():
    time.sleep(0.2)
    x, y = pyautogui.locateCenterOnScreen("confirm.png", confidence=0.9)
    autoit.mouse_move(x, y, speed=2)
    time.sleep(0.25)
    autoit.mouse_click("left")



exit_key = 'esc'
while not keyboard.is_pressed(exit_key):
    if keyboard.is_pressed("alt"):
        ClickDoor()


print("Exiting gracefully...")
# Add any cleanup code here if needed
