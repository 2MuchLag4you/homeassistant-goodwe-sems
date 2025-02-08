from __future__ import annotations

from custom_components.goodwe_sems.const import (DOMAIN, LOGGER,
                                                 SERVICE_OBJECTS,
                                                 SERVICE_PRODUCTION,
                                                 SERVICE_SOLARPANELS, SERVICES)
from custom_components.goodwe_sems.entity.sensorentity import \
    GoodweSemsSensorEntity
from homeassistant.components.sensor import (SensorDeviceClass,
                                             SensorEntityDescription,
                                             SensorStateClass)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfEnergy, UnitOfTime
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

SENSORS: dict[
    SERVICE_OBJECTS, tuple[SensorEntityDescription, ...]
] = {
    SERVICE_PRODUCTION: (

        SensorEntityDescription(
            key="production_status",
            name="Production status",
            icon="mdi:power-settings",
        ),
        SensorEntityDescription(
            key="update_time",
            name="Time of last update",
            icon="mdi:calendar-clock"
        ),
        SensorEntityDescription(
            key="started_time",
            name="Time of the start of solar",
            icon="mdi:calendar-clock"
        ),
        SensorEntityDescription(
            key="power_production",
            name="Power production today",
            icon="mdi:solar-power",
            entity_registry_enabled_default=True,
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING
        )
    ),
    SERVICE_SOLARPANELS: (
        SensorEntityDescription(
            key="station_id",
            name="Station identifier",
            icon="mdi:antenna"
        ),
        SensorEntityDescription(
            key="station_serialnumber",
            name="Station serialnumber",
            icon="mdi:antenna"
        ),
        SensorEntityDescription(
            key="station_name",
            name="Station name",
            icon="mdi:antenna"
        ),
        SensorEntityDescription(
            key="station_model",
            name="Time of the start of solar",
            icon="mdi:antenna"
        ),
        SensorEntityDescription(
            key="station_temprature",
            name="Time of the start of solar",
            icon="mdi:thermostat"
        ),
        SensorEntityDescription(
            key="started_time",
            name="Time of the start of solar",
            icon="mdi:calendar-clock"
        ),
        SensorEntityDescription(
            key="update_time",
            name="Time of last update",
            icon="mdi:calendar-clock"
        ),
        SensorEntityDescription(
            key="total_produced",
            name="Total produced",
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING
        ),
        SensorEntityDescription(
            key="total_hours",
            name="Total hours",
            entity_registry_enabled_default=True,
            native_unit_of_measurement=UnitOfTime.HOURS,
            state_class=SensorStateClass.TOTAL_INCREASING
        ),
        SensorEntityDescription(
            key="total_produced_month",
            name="Total produced month",
            icon="mdi:solar-power",
            entity_registry_enabled_default=True,
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING
        )
    )
}


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    LOGGER.debug("Tried setting up sensor")
    async_add_entities(
        GoodweSemsSensorEntity(
            coordinator=hass.data[DOMAIN][entry.entry_id],
            description=description,
            service_key=service_key,
            name=entry.title,
            service=SERVICES[service_key],
        )
        for service_key, service_sensors in SENSORS.items()
        for description in service_sensors
    )
