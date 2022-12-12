
import logging
from datetime import timedelta
from typing import Final, Literal

from homeassistant.const import Platform

NAME_LONG: str = "GOODWE SEMS Portal (Custom module)"
NAME_SHORT: str = "Goodwe SEMS"
DOMAIN: str = "goodwe_sems"
VERSION: float = 1.0
LOGGER = logging.getLogger(__package__)
MANUFACTURER: str = "Goodwe_SEMS"

UPDATE_INTERVAL: timedelta = timedelta(seconds=300)

# http://www.goodwe-power.com:82/Help - API details
CONF_STATION_ID: str = "station_id"
SEMS_URL: str = "https://www.semsportal.com"
SEMS_API_URL: str = SEMS_URL + "/api/v1/Common/CrossLogin"
SEMS_POWERSTATION_API_URL: str = SEMS_URL + \
    "/api/v3/PowerStation/GetMonitorDetailByPowerstationId"
REQUEST_TIMEOUT: int = 30

PACKAGE_NAME: str = "custom_components.{DOMAIN}"

PLATFORMS: list = [Platform.SENSOR]

SERVICE_PRODUCTION: Final = "production"
SERVICE_SOLARPANELS: Final = "solarpanels"

SERVICES: dict[str, str] = {
    SERVICE_SOLARPANELS: "SolarPanels",
    SERVICE_PRODUCTION: "Production"
}

SERVICE_OBJECTS: Literal = Literal["production", "solarpanels"]
