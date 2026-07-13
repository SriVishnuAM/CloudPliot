import ctypes

user32 = ctypes.windll.user32


def mouse_position():
    class POINT(ctypes.Structure):
        _fields_ = [
            ("x", ctypes.c_long),
            ("y", ctypes.c_long)
        ]

    pt = POINT()

    user32.GetCursorPos(ctypes.byref(pt))

    return pt.x, pt.y


def screen_size():
    return (
        user32.GetSystemMetrics(0),
        user32.GetSystemMetrics(1)
    )