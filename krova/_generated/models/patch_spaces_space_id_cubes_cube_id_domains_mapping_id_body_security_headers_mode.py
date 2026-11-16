from enum import Enum


class PatchSpacesSpaceIdCubesCubeIdDomainsMappingIdBodySecurityHeadersMode(str, Enum):
    APP_MANAGED = "app_managed"
    ENFORCED = "enforced"

    def __str__(self) -> str:
        return str(self.value)
