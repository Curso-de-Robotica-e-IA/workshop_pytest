import logging
import pytest

from meu_modulo.gripper import Gripper, GripperState


def test_gripper_open():
    gripper = Gripper()
    gripper.open()
    assert gripper.state == GripperState.OPENED


def test_gripper_close():
    gripper = Gripper()
    gripper.close()
    assert gripper.state == GripperState.CLOSED


@pytest.fixture
def gripper():
    return Gripper()


def test_gripper_open_with_fixture(gripper):
    gripper.open()
    assert gripper.state == GripperState.OPENED


def test_gripper_close_with_fixture(gripper):
    gripper.close()
    assert gripper.state == GripperState.CLOSED
