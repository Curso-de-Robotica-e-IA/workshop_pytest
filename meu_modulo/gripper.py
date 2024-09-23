import time

from enum import Enum
from logging import getLogger


class GripperState(Enum):
    OPENED = 0
    CLOSED = 1


class Gripper:
    def __init__(self, name="Gripper"):
        self.name = name
        self.state = GripperState.OPENED
        self.logger = getLogger(__name__)

    def open(self):
        self.logger.info(f"{self.name}: abrindo")
        time.sleep(1)
        self.state = GripperState.OPENED

    def close(self):
        self.logger.info(f"{self.name}: fechando")
        time.sleep(1)
        self.state = GripperState.CLOSED
