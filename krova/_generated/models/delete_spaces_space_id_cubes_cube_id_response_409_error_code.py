from enum import Enum


class DeleteSpacesSpaceIdCubesCubeIdResponse409ErrorCode(str, Enum):
    TERMINATION_PROTECTED = "termination_protected"

    def __str__(self) -> str:
        return str(self.value)
