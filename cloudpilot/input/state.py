"""
CloudPilot
Input State

This file contains the current state of every analog and digital input.
Everything writes to this object.
Everything reads from this object.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Stick:
    x: float = 0.0
    y: float = 0.0


@dataclass
class Triggers:
    left: float = 0.0
    right: float = 0.0


@dataclass
class FlightState:

    # Left stick (pitch / roll)
    left_stick: Stick

    # Right stick (camera)
    right_stick: Stick

    # Triggers
    triggers: Triggers

    # Analog controls
    rudder: float = 0.0
    throttle: float = 0.0

    # Buttons
    gear: bool = False
    parking_brake: bool = False

    # Modes
    flight_mode: bool = True
    freelook_mode: bool = False
    interaction_mode: bool = False

    # Trim
    trim_lock: bool = False


def create_state() -> FlightState:
    return FlightState(
        left_stick=Stick(),
        right_stick=Stick(),
        triggers=Triggers(),
    )