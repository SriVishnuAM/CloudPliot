import vgamepad as vg

pad = vg.VX360Gamepad()


class Controller:

    def __init__(self):

        self.x = 0
        self.y = 0

    def left_stick(self, x, y):

        self.x = x
        self.y = y

        pad.left_joystick(
            x_value=x,
            y_value=y
        )

        pad.update()


controller = Controller()