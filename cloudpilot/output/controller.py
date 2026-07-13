"""
CloudPilot
Virtual Xbox Controller

The only module allowed to communicate with vgamepad.
"""

from __future__ import annotations

from dataclasses import dataclass

import vgamepad as vg


@dataclass(slots=True)
class Stick:
    x: int = 0
    y: int = 0


class XboxController:

    def __init__(self):

        self.pad = vg.VX360Gamepad()

        self.left = Stick()
        self.right = Stick()

        self.lt = 0
        self.rt = 0

    def update(self):

        self.pad.left_joystick(
            x_value=self.left.x,
            y_value=self.left.y
        )

        self.pad.right_joystick(
            x_value=self.right.x,
            y_value=self.right.y
        )

        self.pad.left_trigger(self.lt)
        self.pad.right_trigger(self.rt)

        self.pad.update()

    def reset(self):

        self.left = Stick()
        self.right = Stick()

        self.lt = 0
        self.rt = 0

        self.update()