import vgamepad as vg

gamepad = vg.VX360Gamepad()


def update(x, y):

    gamepad.left_joystick(
        x_value=x,
        y_value=y
    )

    gamepad.update()