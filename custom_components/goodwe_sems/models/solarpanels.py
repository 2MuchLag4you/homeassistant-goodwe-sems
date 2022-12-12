
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SolarPanels: 

    station_id: str | None
    station_serialnumber: str | None
    station_name: str | None
    station_model: str | None
    station_temprature: float | None

    started_time: str | None
    update_time: str | None
    
    total_produced: float | None
    total_hours: float | None
    total_produced_month: float | None

    @staticmethod
    def process (data: dict[str, Any]) -> SolarPanels:
        return SolarPanels (
            station_id=data["inverter"][0]["invert_full"]["powerstation_id"],
            station_serialnumber=data["inverter"][0]["invert_full"]["sn"],
            station_name=data["inverter"][0]["invert_full"]["name"],
            station_model=data["inverter"][0]["invert_full"]["model_type"],
            station_temprature=data["inverter"][0]["invert_full"]["tempperature"],
            started_time=data["info"]["turnon_time"],
            update_time=data["info"]["time"],
            total_produced=data["kpi"]["total_power"],
            total_hours=data["inverter"][0]["invert_full"]["hour_total"],
            total_produced_month=data["kpi"]["month_generation"]
        )
