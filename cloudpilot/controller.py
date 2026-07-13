"""
CloudPilot
Xbox Controller Wrapper

This module is the ONLY place that communicates with vgamepad.
Every other part of the application should talk to this class.
"""

from __future__ import annotations

from dataclasses import dataclass

import vgamepad as vg


STICK_MIN = -32768
STICK_MAX = 32767


def clamp_stick(value: int) -> int:
    return max(STICK_MIN, min(STICK_MAX, int(value)))


@dataclass
class StickState:
    x: int = 0
    y: int = 0


class XboxController:
    def __init__(self) -> None:
        self._pad = vg.VX360Gamepad()

        self.left = StickState()
        self.right = StickState()

        self.left_trigger = 0
        self.right_trigger = 0

    def update(self) -> None:
        self._pad.update()

    # ----------------------------
    # Left Stick
    # ----------------------------

    def set_left_stick(self, x: int, y: int) -> None:
        x = clamp_stick(x)
        y = clamp_stick(y)

        self.left.x = x
        self.left.y = y

        self._pad.left_joystick(
            x_value=x,
            y_value=y
        )

    # ----------------------------
    # Right Stick
    # ----------------------------

    def set_right_stick(self, x: int, y: int) -> None:
        x = clamp_stick(x)
        y = clamp_stick(y)

        self.right.x = x
        self.right.y = y

        self._pad.right_joystick(
            x_value=x,
            y_value=y
        )

    # ----------------------------
    # Triggers
    # ----------------------------

    def set_left_trigger(self, value: int) -> None:
        value = max(0, min(255, int(value)))

        self.left_trigger = value

        self._pad.left_trigger(value)

    def set_right_trigger(self, value: int) -> None:
        value = max(0, min(255, int(value)))

        self.right_trigger = value

        self._pad.right_trigger(value)

    # ----------------------------
    # Buttons
    # ----------------------------

    def press(self, button) -> None:
        self._pad.press_button(button)

    def release(self, button) -> None:
        self._pad.release_button(button)

    # ----------------------------
    # Reset
    # ----------------------------

    def reset(self) -> None:
        self.set_left_stick(0, 0)
        self.set_right_stick(0, 0)
        self.set_left_trigger(0)
        self.set_right_trigger(0)
        self.update()