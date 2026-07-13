from __future__ import annotations

import time

from cloudpilot.input.input_manager import InputManager


class CloudPilot:

    def __init__(self):

        self.running = False

        self.input = InputManager()

    def initialize(self):

        self.input.initialize()

    def shutdown(self):

        self.input.shutdown()

    def update(self):

        self.input.update()

        time.sleep(1 / 240)

    def run(self):

        self.initialize()

        self.running = True

        try:

            while self.running:

                self.update()

        except KeyboardInterrupt:

            pass

        self.shutdown()