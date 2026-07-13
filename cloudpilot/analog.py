class AnalogAxis:
    def __init__(self, speed=5.0):
        self.value = 0.0
        self.target = 0.0
        self.speed = speed

    def update(self, dt):
        diff = self.target - self.value

        step = self.speed * dt

        if abs(diff) < step:
            self.value = self.target
        else:
            self.value += step if diff > 0 else -step

    def set(self, value):
        self.target = max(-1.0, min(1.0, value))

    def reset(self):
        self.target = 0.0