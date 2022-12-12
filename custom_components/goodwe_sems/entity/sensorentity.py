from __future__ import annotations

from custom_components.goodwe_sems.const import (DOMAIN, MANUFACTURER,
                                                 SERVICE_OBJECTS)
from custom_components.goodwe_sems.tasks import ModuleDataUpdateCoordinator
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.components.sensor import (SensorEntity,
                                             SensorEntityDescription)
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity


class GoodweSemsSensorEntity(CoordinatorEntity, SensorEntity):

    coordinator: ModuleDataUpdateCoordinator

    def __init__(
        self,
        *,
        coordinator: ModuleDataUpdateCoordinator,
        description: SensorEntityDescription,
        service_key: SERVICE_OBJECTS,
        name: str,
        service: str
    ) -> None:
        super().__init__(coordinator=coordinator)
        self._service_key = service_key

        self.entity_id = "{0}.{1}_{2}".format(
            SENSOR_DOMAIN, name, description.key)
        self.entity_description = description
        self._attr_unique_id = (
            "{0}_{1}_{2}".format(
                coordinator.config_entry.entry_id, service_key, description.key)
        )

        self._attr_device_info = DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={
                (DOMAIN, "{0}_{1}".format(
                    coordinator.config_entry.entry_id, service_key))
            },
            manufacturer=MANUFACTURER,
            name=service
        )

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""
        value = getattr(
            self.coordinator.data[self._service_key], self.entity_description.key
        )
        if isinstance(value, str):
            return value.lower()
        return value
