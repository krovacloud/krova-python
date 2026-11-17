from enum import Enum


class BackupShareStatus(str, Enum):
    ACCEPTED = "accepted"
    CANCELED = "canceled"
    DECLINED = "declined"
    EXPIRED = "expired"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
