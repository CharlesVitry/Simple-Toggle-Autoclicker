from pynput.mouse import Button,Controller,Listener
from time import sleep
import numpy as np

mouse = Controller()
running = True
pause = True

def on_click(x, y, button, pressed):
    global pause
    if pressed and button==Button.middle :
        pause = False
    elif(not pressed  and button==Button.middle):
        pause = True

listener = Listener(
    on_click=on_click)
listener.start()

while running:
    sleep(abs((np.random.normal(48, 35, 1) * 0.001)[0]))
    if not pause:
        mouse.press(Button.left)
        sleep((np.random.gamma(43, 1, 1) * 0.001)[0])
        mouse.release(Button.left)


