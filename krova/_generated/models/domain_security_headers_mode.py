from enum import Enum


class DomainSecurityHeadersMode(str, Enum):
    APP_MANAGED = "app_managed"
    ENFORCED = "enforced"

    def __str__(self) -> str:
        return str(self.value)
