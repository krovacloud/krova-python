from enum import Enum


class DnsRecordStatusState(str, Enum):
    FOUND = "found"
    MISMATCH = "mismatch"
    MISSING = "missing"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
