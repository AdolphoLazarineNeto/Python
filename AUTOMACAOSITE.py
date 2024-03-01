import pyautogui
import time


pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("Backspace")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://github.com/AdolphoLazarineNeto")
pyautogui.press("enter")
pyautogui.click(x=294, y=14)
time.sleep(3)
pyautogui.write("https://www.linkedin.com/in/adolpho-lazarine-neto-3148a821b/")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=490, y=560)
time.sleep(2)
pyautogui.click(x=1158, y=331)
time.sleep(2)
