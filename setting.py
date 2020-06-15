"""
Global setting of VN Trader.
"""

from logging import CRITICAL,INFO,DEBUG
from typing import Dict, Any
from tzlocal import get_localzone

from .utility import load_json

SETTINGS: Dict[str, Any] = {
    "font.family": "Arial",
    "font.size": 12,

    "log.active": True,
    "log.level": DEBUG,
    "log.console": True,
    "log.file": True,

    "email.server": "smtp.qq.com",
    "email.port": 465,
    "email.username": "",
    "email.password": "",
    "email.sender": "",
    "email.receiver": "",

    "rqdata.username": "070150",
    "rqdata.password": "122244",

    "database.timezone": get_localzone().zone,
    "database.driver": "mysql",                # see database.Driver
    "database.database": "runoob",         # for sqlite, use this as filepath
    "database.host": "localhost",
    "database.port": 3306,
    "database.user": "root",
    "database.password": "1234",
    "database.authentication_source": "admin",  # for mongodb
}

# Load global setting from json file.
SETTING_FILENAME: str = "vt_setting.json"
SETTINGS.update(load_json(SETTING_FILENAME))


def get_settings(prefix: str = "") -> Dict[str, Any]:
    prefix_length = len(prefix)
    return {k[prefix_length:]: v for k, v in SETTINGS.items() if k.startswith(prefix)}
