from __future__ import annotations

class SemsStatus:
    ONLINE = "online"
    OFFLINE = "offline"
    NEUTRAL = "switching state"

def define_sems_status(status_input: int) -> str:
    """Get current status of sems"""
    if status_input == 0:
        return SemsStatus.NEUTRAL
    elif status_input == 1:
        return SemsStatus.OFFLINE
    return SemsStatus.ONLINE

