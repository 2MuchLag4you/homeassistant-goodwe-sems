
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from aiohttp import ClientSession
from custom_components.goodwe_sems.models import Production, SolarPanels
from custom_components.goodwe_sems.tasks import fetch


@dataclass 
class Sems:
    def __init__(self, name: str, password: str, station_id: str, session: ClientSession) -> None:
        self._name = name
        self._password = password
        self._station_id = station_id
        self._session = session
        self._attributes = {}

    async def request(self) -> dict[str, Any]:
        if not bool(self._attributes):
            self._attributes = await fetch(username=self._name, password=self._password, station_id=self._station_id, session=self._session)
        return self._attributes

    async def clear(self):
        self._attributes = {}
        return None

    async def solarpanels(self) -> SolarPanels:
        fetched_data = await self.request()
        return SolarPanels.process(fetched_data)

    async def production(self) -> Production:
        fetched_data = await self.request()
        return Production.process(fetched_data)
    
    async def __aenter__(self) -> Sems:
        return self

    async def __aexit__(self, *_exc_info) -> None:
        return None
