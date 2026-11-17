from enum import Enum


class PostSpacesSpaceIdCubesCubeIdResizeResponse200State(str, Enum):
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
