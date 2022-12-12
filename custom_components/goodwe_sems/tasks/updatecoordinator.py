
from custom_components.goodwe_sems.classes import ModuleData, Sems
from custom_components.goodwe_sems.const import (CONF_STATION_ID, DOMAIN,
                                                 LOGGER, SERVICE_PRODUCTION,
                                                 SERVICE_SOLARPANELS,
                                                 UPDATE_INTERVAL)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers import aiohttp_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator


class ModuleDataUpdateCoordinator(DataUpdateCoordinator[ModuleData]):
    config_entry = ConfigEntry

    def __init__(self, hass: HomeAssistant) -> None:
        super().__init__(
            hass, 
            logger=LOGGER,
            name=DOMAIN,
            update_interval=UPDATE_INTERVAL
        )

        self.sems = Sems(
            name=self.config_entry.data[CONF_USERNAME], password=self.config_entry.data[CONF_PASSWORD], station_id=self.config_entry.data[CONF_STATION_ID],session=aiohttp_client.async_get_clientsession(self.hass)
        )

    async def _async_update_data(self) -> ModuleData:
        LOGGER.debug("")

        await self.sems.clear()

        data = {
            SERVICE_PRODUCTION: await self.sems.production(),
            SERVICE_SOLARPANELS: await self.sems.solarpanels()
        }

        return ModuleData(data)
