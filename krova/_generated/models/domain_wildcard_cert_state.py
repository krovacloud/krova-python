from enum import Enum


class DomainWildcardCertState(str, Enum):
    FAILED = "failed"
    ISSUING = "issuing"
    PENDING_DELEGATION = "pending_delegation"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
