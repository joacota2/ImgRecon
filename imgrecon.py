import time
import keyboard
import pyautogui
import pywin32
import win32con

time.sleep(5)


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)


while not keyboard.is_pressed('q'):
    start = pyautogui.locateCenterOnScreen('tMW.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    if start is not None:
        pyautogui.moveTo(start)  # Moves the mouse to the coordinates of the image
        click()
