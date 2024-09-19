import numpy as np


class Position3D:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.__x = x
        self.__y = y
        self.__z = z
        self.__np_repr = np.array([self.x, self.y, self.z], dtype=float)

    def __str__(self) -> str:
        return f"Position3D({self.__x}, {self.__y}, {self.__z})"

    def __repr__(self) -> str:
        return str(self)

    @classmethod
    def from_tuple_of_floats(
        cls,
        position: tuple[float, float, float],
    ):
        return cls(Position3D(*position))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position3D):
            raise ValueError("Comparing Position3D with non-Position3D object")
        return np.all(self.__np_repr == other.__np_repr)

    def __add__(self, other: object) -> "Position3D":
        if not isinstance(other, Position3D):
            raise ValueError("Adding Position3D with non-Position3D object")
        return Position3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: object) -> "Position3D":
        if not isinstance(other, Position3D):
            raise ValueError("Subtracting Position3D with non-Position3D object")
        return Position3D(self.x - other.x, self.y - other.y, self.z - other.z)

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @property
    def z(self) -> float:
        return self.__z

    def rotate(self, angle: float, axis: int = 0, inplace=True) -> "Position3D" | None:
        assert axis in [0, 1, 2], "Axis must be 0, 1 or 2"
        rotation_matrixes = {
            0: np.array(
                [
                    [1, 0, 0],
                    [0, np.cos(angle), -np.sin(angle)],
                    [0, np.sin(angle), np.cos(angle)],
                ]
            ),
            1: np.array(
                [
                    [np.cos(angle), 0, np.sin(angle)],
                    [0, 1, 0],
                    [-np.sin(angle), 0, np.cos(angle)],
                ]
            ),
            2: np.array(
                [
                    [np.cos(angle), -np.sin(angle), 0],
                    [np.sin(angle), np.cos(angle), 0],
                    [0, 0, 1],
                ]
            ),
        }

        rotated_position = np.dot(rotation_matrixes[axis], self.__np_repr)
        if not inplace:
            return Position3D(*rotated_position)
        self.__x, self.__y, self.__z = rotated_position
        self.__np_repr = rotated_position
