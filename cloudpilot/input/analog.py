"""
CloudPilot
Analog axis implementation.

Every analog control (rudder, throttle, trim, camera, etc.)
uses this class.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AnalogAxis:
    """
    Represents a smooth analog value.

    value  -> current output
    target -> desired output
    """

    speed: float = 4.0

    value: float = 0.0
    target: float = 0.0

    def set_target(self, value: float) -> None:
        """Set a new target value."""

        self.target = max(-1.0, min(1.0, value))

    def center(self) -> None:
        """Return to the center."""

        self.target = 0.0

    def update(self, delta_time: float) -> float:
        """
        Move current value toward target.
        """

        difference = self.target - self.value

        step = self.speed * delta_time

        if abs(difference) <= step:
            self.value = self.target
        else:
            if difference > 0:
                self.value += step
            else:
                self.value -= step

        return self.value