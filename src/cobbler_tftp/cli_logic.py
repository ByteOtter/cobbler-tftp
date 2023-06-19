"""
Cobbler-tftp will be managable as a command-line service.
"""

import click
import yaml

from cobbler_tftp.cbl_tftp import CobblerConnection
from cobbler_tftp.settings import SettingsFactory
from cobbler_tftp.utils import print_default_settings

with open("src/cobbler_tftp/config/settings.yml", "r", encoding="utf-8") as stream:
    try:
        SETTINGS = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

_context_settings = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=_context_settings)
def cli():
    pass


@cli.command()
@click.option(
    "--no-daemon",
    "-d",
    is_flag=True,
    default=SETTINGS["daemon"],
    help="Stop cobbler-tftp from running as daemon.",
)
@click.option(
    "--enable-automigration",
    is_flag=True,
    default=SETTINGS["auto_migrate_settings"],
    help="Enable automigration of settings.",
)
@click.option(
    "--config", "-c", type=click.Path(), help="Set location of configuration file."
)
@click.option(
    "--settings",
    "-s",
    multiple=True,
    help="""Set custom settings in format:\n
    <PARENT_YAML_KEY>.<CHILD_YAML_KEY>.<...>.<KEY_NAME>=<VALUE>.\n
    Your settings must use single quotes. If a single quote appears within a value it must be escaped.""",
)
def start(daemon, enable_automigration, config, settings):
    """
    Start the cobbler-tftp server.
    """
    click.echo(
        f"Cobbler-tftpCopyright (c) 2023\nLicensed under the terms of the GPL-v2.0 license.\nInitializing Cobbler-tftp server...\n"
    )
    if daemon:
        click.echo(
            f"'--daemon' flag set.\nCobbler-tftp will be running as a daemon in the background."
        )
    else:
        click.echo(f"Server running...")
        settings_file = SettingsFactory.load_config_file(config)
        environment_variables = SettingsFactory.load_env_variables()
        cli_arguments = SettingsFactory.load_cli_options(
            daemon, enable_automigration, settings
        )
        application_settings = settings.SettingsFactory.build_settings(
            settings_file, environment_variables, cli_arguments
        )
        connection = CobblerConnection(application_settings)


@cli.command()
def version():
    """
    Check cobbler-tftp version. If there are any cobbler servers connected their versions will be printed aswell.
    """
    pass


@cli.command()
def print_default_config():
    """
    Print the default application parameters.
    """
    pass


@cli.command()
def stop():
    """
    Stop the cobbler-tftp server daemon if it is running
    """
    pass
