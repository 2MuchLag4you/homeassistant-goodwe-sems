from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.exceptions import ConfigEntryNotReady

from custom_components.goodwe_sems.tasks import ModuleDataUpdateCoordinator
from custom_components.goodwe_sems.const import (
    DOMAIN,
    PLATFORMS
)

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    update_coordinator = ModuleDataUpdateCoordinator(hass)
    try:
        await update_coordinator.async_config_entry_first_refresh()
    except ConfigEntryNotReady:
        raise

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][config_entry.entry_id] = update_coordinator
    hass.config_entries.async_setup_platforms(config_entry, PLATFORMS)
    return True