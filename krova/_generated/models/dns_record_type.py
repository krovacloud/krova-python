from enum import Enum


class DnsRecordType(str, Enum):
    A = "A"
    CNAME = "CNAME"
    TXT = "TXT"

    def __str__(self) -> str:
        return str(self.value)
