from __future__ import annotations

from typing import Any

import requests
from aiohttp import ClientSession
from custom_components.goodwe_sems.const import (LOGGER, REQUEST_TIMEOUT,
                                                 SEMS_API_URL,
                                                 SEMS_POWERSTATION_API_URL)
from custom_components.goodwe_sems.exceptions import (
    GoodweSemsConnectionError, GoodweSemsEmptyResponseError)


async def fetch(username: str, password: str, station_id: str, session: ClientSession) -> dict[str, Any]:
    http_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'token': '{"version":"v2.1.0","client":"ios","language":"en"}'
    }

    login_data = '{"account":"' + username + '","pwd":"' + password + '"}'

    LOGGER.debug("SEMS - Requesting token from sems api")
    try:
        login_response = await session.post(
            SEMS_API_URL,
            data=login_data,
            headers=http_headers,
            timeout=REQUEST_TIMEOUT
        )
    except requests.exceptions.RequestException:
        raise GoodweSemsConnectionError(
            "Connection to the API could not be made")

    login_json_response = await login_response.json()
    if not bool(login_json_response["data"]):
        raise GoodweSemsEmptyResponseError("No data received from the API")

    request_timestamp = login_json_response["data"]["timestamp"]
    request_uid = login_json_response["data"]["uid"]
    request_token = login_json_response["data"]["token"]
    LOGGER.debug(
        f"SEMS - Fetched information from API, token is {request_token}")

    token_string = '{"version":"v2.1.0","client":"ios","language":"en","timestamp":"' + \
        str(request_timestamp)+'","uid":"' + \
        request_uid + '","token":"'+request_token+'"}'

    http_headers["token"] = token_string
    powerstation_data = '{"powerStationId":"' + station_id + '"}'

    try:
        powerstation_response = await session.post(
            SEMS_POWERSTATION_API_URL,
            data=powerstation_data,
            headers=http_headers,
            timeout=REQUEST_TIMEOUT
        )

    except requests.exceptions.RequestException:
        raise GoodweSemsConnectionError(
            "Connection to the API could not be made")

    if powerstation_response.status != 200:
        raise GoodweSemsConnectionError(
            f"Response did not give the expected response, it gave error {powerstation_response.status}")

    powerstation_json_response = await powerstation_response.json()
    if not bool(powerstation_json_response["data"]):
        raise GoodweSemsEmptyResponseError("No data received from the API")

    return powerstation_json_response["data"]
