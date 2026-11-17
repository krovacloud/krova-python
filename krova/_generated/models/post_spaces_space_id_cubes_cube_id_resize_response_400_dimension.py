from enum import Enum


class PostSpacesSpaceIdCubesCubeIdResizeResponse400Dimension(str, Enum):
    CPU = "cpu"
    DISK = "disk"
    RAM = "ram"

    def __str__(self) -> str:
        return str(self.value)
