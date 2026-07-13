import math

STICK_MAX = 32767


def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))


def normalize(value, minimum, maximum):
    return (value - minimum) / (maximum - minimum)


def apply_deadzone(x, y, deadzone):
    mag = math.sqrt(x * x + y * y)

    if mag < deadzone:
        return 0.0, 0.0

    scale = (mag - deadzone) / (1.0 - deadzone)

    if mag != 0:
        x = (x / mag) * scale
        y = (y / mag) * scale

    return x, y


def apply_curve(value, exponent):
    sign = -1 if value < 0 else 1
    return sign * (abs(value) ** exponent)


def stick(value):
    return int(clamp(value, -1.0, 1.0) * STICK_MAX)