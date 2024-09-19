from meu_modulo.arm import Arm
from meu_modulo.gripper import Gripper
from meu_modulo.utils import Position3D


class PickAndPlaceRobot:
    def __init__(self, arm: Arm, gripper: Gripper):
        self.arm = arm
        self.gripper = gripper

    def pick(self, position: Position3D):
        self.arm.move_to(position)
        self.gripper.close()
        self.arm.move_relative(Position3D(0, 0, 0.1))

    def place(self, position: Position3D):
        self.arm.move_to(position)
        self.arm.move_relative(Position3D(0, 0, -0.1))
