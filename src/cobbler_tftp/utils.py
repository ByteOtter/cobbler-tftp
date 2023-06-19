"""
This file provides helper functions for use in the cli.
"""
from typing import Any, Dict

import yaml

try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files


def print_default_settings() -> None:
    """
    Load the default config file and print its values out.
    """
    _settings_dict: dict = {}

    try:
        config_file_content = (
            files("cobbler_tftp.settings.data").joinpath("settings.yml").read_text()
        )
        _settings_dict = yaml.safe_load(config_file_content)
    except yaml.YAMLError as exc:
        print(f"{exc}: No valid default configuration found!")

    for k, v in _settings_dict.items():
        print(k + ": " + v + "\n")
