"""
CloudPilot
Mouse Engine
"""

from __future__ import annotations

import ctypes

from cloudpilot.input.mapper import Mapper


class POINT(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_long),
        ("y", ctypes.c_long),
    ]


class MouseEngine:

    def __init__(self, state):

        self.state = state

        self.user32 = ctypes.windll.user32

        self.mapper = Mapper()

    def get_position(self):

        point = POINT()

        self.user32.GetCursorPos(ctypes.byref(point))

        return point.x, point.y

    def update(self):

        x, y = self.get_position()

        nx, ny = self.mapper.map(x, y)

        self.state.left_stick.x = nx
        self.state.left_stick.y = ny