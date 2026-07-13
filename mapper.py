def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def normalize(value, minimum, maximum):
    return (value - minimum) / (maximum - minimum)


def remap(value):

    if abs(value) < 0.03:
        return 0

    return int(value * 32767)