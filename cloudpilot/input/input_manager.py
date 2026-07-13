"""
CloudPilot
Input Manager

Responsible for updating every input device and exposing a
single FlightState object to the rest of the application.
"""

from __future__ import annotations

from cloudpilot.input.state import create_state, FlightState
from cloudpilot.input.mouse import MouseEngine
from cloudpilot.input.keyboard import KeyboardEngine


class InputManager:

    def __init__(self) -> None:

        self.state: FlightState = create_state()

        self.mouse = MouseEngine(self.state)
        self.keyboard = KeyboardEngine(self.state)

    def initialize(self):

        self.keyboard.start()

    def shutdown(self):

        self.keyboard.stop()

    def update(self):

        self.mouse.update()