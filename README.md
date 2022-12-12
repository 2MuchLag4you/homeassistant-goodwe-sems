# HomeAssistant - Goodwe Sems
The ``Goodwe Sems`` platform offers an energy integration using the API of goodwe.  This addon can be used as energy source for the solar panels.

# Configuration 

Adding the ``Goodwe Sems`` to your Home Assistant can be done via the user interface, after the integration has been added to the ``custom_components`` . 

* Add the goodwe_sems folder inside the ``config/custom_components`` 
* Restart Home Assistant 
* In the side bar click on ``Settings`` 
* From the configuration menu go to ``Devices & Services`` 
* In the bottom right, click the ``Add Integration`` button.
* Select the "**SEMS Sensor**" from the list
* Follow the configuration instructions on screen to complete the setup

## Sensors
The integrations that will be added after the integration.

**Sensor** | **Measurement method** 
---|---
sems_sensor_power_production | Current production kWh 
sems_sensor_production_status | Status of the sensor
sems_sensor_station_id | Unique identifier
sems_sensor_station_name | Unique station name
sems_sensor_station_serialnumber | Unique station serial number
sems_sensor_station_model | Station model 
sems_sensor_update_time | Time of last update
sems_sensor_started_time | Time of first start
sems_sensor_total_hours | Time of total amount of solar hours
sems_sensor_total_produced | Total produced kWh
sems_sensor_total_produced_month | Total produced kWh this month
