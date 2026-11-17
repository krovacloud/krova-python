from enum import Enum


class BackupStatus(str, Enum):
    COMPLETE = "complete"
    CREATING = "creating"
    FAILED = "failed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
