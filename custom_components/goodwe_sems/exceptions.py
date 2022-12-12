class GoodweSemsError(Exception):
    """Generic Goodwe Sems error"""


class GoodweSemsConnectionError(Exception):
    """Default connection error for Goodwe sems"""


class GoodweSemsConnectionTimeOutError(Exception):
    """Connection timeout error for Goodwe Sems"""


class GoodweSemsEmptyResponseError(Exception):
    """Communication gave no output"""
