from typing import TypedDict

from custom_components.goodwe_sems.models import Production, SolarPanels


class ModuleData(TypedDict):
    """Class for defining data in module"""
    prodcution: Production
    solarpanels: SolarPanels
