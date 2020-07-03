import pyautogui
from time import sleep
import webbrowser
import socket
import time

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

while is_connected()==False:
        print("waiting for internet access.....")
        time.sleep(2)

print("Enter a list of names and their messages:\n")
contacts={}
for i in range(n):
    contact=input("Enter a name: ")


pyautogui.hotkey("win","d")
webbrowser.open("https://web.whatsapp.com/")
sleep(20)
pyautogui.press('tab',2)
# for contact in contacts:
pyautogui.typewrite("dino")
sleep(2)
pyautogui.press('tab')
sleep(2)
pyautogui.press('tab',2)
pyautogui.typewrite("lololol")
pyautogui.press("enter")
pyautogui.press('tab')

