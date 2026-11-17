from enum import Enum


class PostSpacesSpaceIdCubesImportsBodySshKeyMode(str, Enum):
    KEEP = "keep"
    REPLACE = "replace"

    def __str__(self) -> str:
        return str(self.value)
