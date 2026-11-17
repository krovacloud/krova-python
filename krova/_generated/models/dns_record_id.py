from enum import Enum


class DnsRecordId(str, Enum):
    CERTIFICATE = "certificate"
    OWNERSHIP = "ownership"
    ROUTING = "routing"

    def __str__(self) -> str:
        return str(self.value)
