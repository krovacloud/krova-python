from enum import Enum


class GetSpacesSpaceIdCubesImportsImportIdResponse200ImportStatus(str, Enum):
    COMPLETE = "complete"
    EXPIRED = "expired"
    FAILED = "failed"
    FINALIZING = "finalizing"
    PROVISIONING = "provisioning"
    UPLOADING = "uploading"

    def __str__(self) -> str:
        return str(self.value)
