"""
CloudPilot
Input filters
"""

from __future__ import annotations

import math


class DeadzoneFilter:

    def __init__(self, deadzone: float = 0.04):
        self.deadzone = deadzone

    def process(self, x: float, y: float):

        magnitude = math.sqrt(x * x + y * y)

        if magnitude <= self.deadzone:
            return 0.0, 0.0

        scale = (magnitude - self.deadzone) / (1.0 - self.deadzone)

        if magnitude != 0:
            x = (x / magnitude) * scale
            y = (y / magnitude) * scale

        return x, y


class CurveFilter:

    def __init__(self, exponent: float = 1.6):
        self.exponent = exponent

    def process(self, value: float):

        sign = -1 if value < 0 else 1

        return sign * (abs(value) ** self.exponent)


class SmoothFilter:

    def __init__(self, factor: float = 0.15):

        self.factor = factor

        self.x = 0.0
        self.y = 0.0

    def process(self, x: float, y: float):

        self.x += (x - self.x) * self.factor
        self.y += (y - self.y) * self.factor

        return self.x, self.y