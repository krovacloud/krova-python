from enum import Enum


class CubeState(str, Enum):
    BOOTING = "booting"
    DELETED = "deleted"
    ERROR = "error"
    PENDING = "pending"
    RESIZING = "resizing"
    RUNNING = "running"
    STOPPED = "stopped"
    STOPPING = "stopping"

    def __str__(self) -> str:
        return str(self.value)
