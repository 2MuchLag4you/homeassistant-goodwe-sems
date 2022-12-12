
from typing import Any

import voluptuous as vol
from custom_components.goodwe_sems.classes import Sems
from custom_components.goodwe_sems.const import CONF_STATION_ID, DOMAIN, LOGGER
from custom_components.goodwe_sems.exceptions import GoodweSemsError
from homeassistant import config_entries
from homeassistant.config_entries import ConfigFlow
from homeassistant.const import CONF_NAME, CONF_PASSWORD, CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import aiohttp_client


@config_entries.HANDLERS.register(DOMAIN)
class GoodweSemsFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION = 1
    _errors = {}

    async def async_step_user(
        self, user_input: dict[str, Any] = None
    ) -> FlowResult:
        self._errors = {}
        if user_input is not None:
            try:
                LOGGER.debug("SEMS - Trying to initialize first sync")
                async with Sems(
                    name=user_input[CONF_USERNAME],
                    password=user_input[CONF_PASSWORD],
                    station_id=user_input[CONF_STATION_ID],
                    session=aiohttp_client.async_get_clientsession(self.hass)
                ) as client:
                    await client.solarpanels()
            except GoodweSemsError:
                self._errors["base"] = "cannot_connect"
            else:
                return self.async_create_entry(
                    title=user_input[CONF_NAME],
                    data={
                        CONF_USERNAME: user_input[CONF_USERNAME],
                        CONF_PASSWORD: user_input[CONF_PASSWORD],
                        CONF_STATION_ID: user_input[CONF_STATION_ID]
                    }
                )
        LOGGER.debug("Requesting information from user")
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Optional(CONF_NAME, default="SEMS Sensor"): str,
                    vol.Required(CONF_USERNAME): str,
                    vol.Required(CONF_PASSWORD): str,
                    vol.Required(CONF_STATION_ID): str
                }
            ),
            errors=self._errors
        )
