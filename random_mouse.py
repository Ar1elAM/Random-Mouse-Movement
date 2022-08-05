from pynput.mouse import Button, Controller
import pyautogui
import random
import time

x = 0
pyautogui.FAILSAFE = False
mouse = Controller()
while (x <= 5):
    pyautogui.moveRel(0, 100)
    pyautogui.moveRel(-100, 0)
    pyautogui.moveRel(-4000, -3000)
    x += 1
current_mouse_pos = mouse.position
x_limit = (current_mouse_pos)
x = 0
while (x <= 5):
    pyautogui.moveRel(0, -100)
    pyautogui.moveRel(100, 0)
    pyautogui.moveRel(4000, 3000)
    x += 1
current_mouse_pos = mouse.position
y_limit = (current_mouse_pos)
print(x_limit, "\n", y_limit)
while True:
    r_x = random.randint(int(x_limit[0]), int(y_limit[0]))
    r_y = random.randint(int(x_limit[1]), int(y_limit[1]))
    r_timer = round(random.uniform(30, 120), 2)
    print(r_x, r_y, r_timer)
    timer = (r_timer)
    pos_x = (r_x)
    pos_y = (r_y)
    pyautogui.moveTo(pos_x, pos_y)
    time.sleep(r_timer)