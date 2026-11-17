from enum import Enum


class PostSpacesSpaceIdCubesCubeIdResizeResponse400Code(str, Enum):
    INSUFFICIENT_HOST_CAPACITY = "insufficient_host_capacity"

    def __str__(self) -> str:
        return str(self.value)
