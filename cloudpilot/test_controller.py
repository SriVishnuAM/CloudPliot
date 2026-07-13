import time
import vgamepad as vg

print("Creating virtual Xbox controller...")

gamepad = vg.VX360Gamepad()

print("Controller created!")

# Press A
gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()

print("Pressed A")
time.sleep(1)

# Release A
gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()

print("Released A")

# Move left stick in a circle
for i in range(360):
    import math

    x = int(math.cos(math.radians(i)) * 32767)
    y = int(math.sin(math.radians(i)) * 32767)

    gamepad.left_joystick(x_value=x, y_value=y)
    gamepad.update()
    time.sleep(0.01)

gamepad.left_joystick(0, 0)
gamepad.update()

print("Done.")