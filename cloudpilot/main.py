import time
import keyboard

from mouse_engine import *
from mapper import *
from controller import controller
from config import *

width, height = screen_size()

sx = 0.0
sy = 0.0

while True:

    if keyboard.is_pressed("esc"):
        break

    mx, my = mouse_position()

    nx = normalize(mx, 0, width)
    ny = normalize(my, 0, height)

    nx = nx * 2 - 1
    ny = ny * 2 - 1

    ny *= -1

    nx, ny = apply_deadzone(nx, ny, DEADZONE)

    nx = apply_curve(nx, CURVE)
    ny = apply_curve(ny, CURVE)

    sx += (nx - sx) * SMOOTHING
    sy += (ny - sy) * SMOOTHING

    controller.left_stick(
        stick(sx),
        stick(sy)
    )

    time.sleep(1 / FPS)

controller.left_stick(0, 0)