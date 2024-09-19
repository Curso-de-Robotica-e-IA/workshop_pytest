from logging import getLogger

from meu_modulo.utils import Position3D


class Arm:
    def __init__(self, name, position: Position3D):
        self.name = name
        self.position = position
        self.logger = getLogger(__name__)

    def move_to(self, position: Position3D):
        self.logger.info(f"{self.name}: movendo para {position}")
        self.position = position

    def move_relative(self, position: Position3D):
        self.position += position
        self.logger.info(f"{self.name}: movendo para {self.position}")
