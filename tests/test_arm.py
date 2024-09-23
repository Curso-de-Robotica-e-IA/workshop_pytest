import logging
import pytest

from meu_modulo.arm import Arm
from meu_modulo.utils import Position3D


@pytest.fixture
def arm():
    return Arm("Arm1", Position3D(0, 0, 0))


@pytest.mark.parametrize(
    "position",
    [
        Position3D(1, 1, 1),
        Position3D(2, 2, 2),
        Position3D(3, 3, 3),
    ],
)
def test_arm_move_to_given_position(arm, position):
    arm.move_to(position)
    assert arm.position == position


@pytest.mark.parametrize(
    "position",
    [
        Position3D(1, 1, 1),
        Position3D(2, 2, 2),
        Position3D(3, 3, 3),
    ],
)
def test_arm_move_relative_given_position(arm, position):
    arm.move_relative(position)
    assert arm.position == position


@pytest.mark.parametrize(
    "position",
    [
        Position3D(1, 1, 1),
        Position3D(2, 2, 2),
        Position3D(3, 3, 3),
    ],
)
def test_arm_move_to_given_position_without_sleep(patch_time_sleep, arm, position):
    arm.move_to(position)
    assert arm.position == position


@pytest.mark.parametrize(
    "position",
    [
        Position3D(1, 1, 1),
        Position3D(2, 2, 2),
        Position3D(3, 3, 3),
    ],
)
def test_arm_move_relative_given_position_without_sleep(patch_time_sleep, arm, position):
    arm.move_relative(position)
    assert arm.position == position


def test_check_if_arm_has_logged_when_move_to(arm, caplog):
    caplog.set_level(logging.INFO)
    arm.move_to(Position3D(1, 1, 1))
    assert "Arm1: movendo para Position3D(1, 1, 1)" in caplog.text


def test_check_if_arm_has_logged_when_move_relative(arm, caplog):
    caplog.set_level(logging.INFO)
    arm.move_relative(Position3D(1, 1, 1))
    assert "Arm1: movendo para Position3D(1, 1, 1)" in caplog.text
