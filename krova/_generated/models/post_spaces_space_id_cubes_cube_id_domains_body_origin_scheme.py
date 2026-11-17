from enum import Enum


class PostSpacesSpaceIdCubesCubeIdDomainsBodyOriginScheme(str, Enum):
    HTTP = "http"
    HTTPS = "https"

    def __str__(self) -> str:
        return str(self.value)
