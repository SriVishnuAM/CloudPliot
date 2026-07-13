import time
import keyboard

from mouse_engine import *
from mapper import *
from controller import *

width, height = screen_size()

print(width, height)

while True:

    if keyboard.is_pressed("esc"):
        break

    mx, my = mouse_position()

    x = normalize(mx, 0, width)
    y = normalize(my, 0, height)

    x = (x * 2) - 1
    y = (y * 2) - 1

    y *= -1

    update(
        remap(x),
        remap(y)
    )

    time.sleep(1 / 240)

update(0, 0)