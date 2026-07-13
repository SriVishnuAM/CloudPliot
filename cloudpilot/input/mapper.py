"""
CloudPilot
Mouse Mapper
"""

from __future__ import annotations

import ctypes


class Mapper:

    def __init__(self):

        user32 = ctypes.windll.user32

        self.width = user32.GetSystemMetrics(0)
        self.height = user32.GetSystemMetrics(1)

    def map(self, x, y):

        nx = (x / self.width) * 2 - 1
        ny = (y / self.height) * 2 - 1

        ny *= -1

        return nx, ny