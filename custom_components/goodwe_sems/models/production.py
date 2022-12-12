

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from custom_components.goodwe_sems.utils import define_sems_status


@dataclass
class Production:

    production_status : str | None
    update_time: str | None
    started_time: str | None

    power_production: float | None
    
    @staticmethod
    def process (data: dict[str, Any]) -> Production:
        return Production (
            production_status=define_sems_status(data["info"]["status"]),
            started_time=data["info"]["turnon_time"],
            update_time=data["info"]["time"],
            power_production=data["inverter"][0]["invert_full"]["eday"]
        )
