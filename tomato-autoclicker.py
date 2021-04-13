from pynput.mouse import Button, Controller
import time
import keyboard
mouse = Controller()
print("by DomatesGames (Github username.)")
startkey = input("Start Autoclick on which key is pressed? ")
stopkey = input("Stop Autoclick on which key is pressed?")
print("Started, please press " + startkey + " for start. Please press " + stopkey + " for stop Autoclick.")
while(True):
    if keyboard.is_pressed(startkey):
        while(True):
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(0.01)
            if keyboard.is_pressed(stopkey):
                break
