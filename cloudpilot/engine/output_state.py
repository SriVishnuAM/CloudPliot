from dataclasses import dataclass, field


@dataclass(slots=True)
class Stick:
    x: int = 0
    y: int = 0


@dataclass(slots=True)
class OutputState:
    left: Stick = field(default_factory=Stick)
    right: Stick = field(default_factory=Stick)
    left_trigger: int = 0
    right_trigger: int = 0