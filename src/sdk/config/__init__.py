"""Main module for handling all of the microservice's configurations.

This package features modules for managing app configurations and settings.

  Usage example:

  from sdk.config import ConfigBase
  
  if ConfigBase().is_development_env:
      Run development environment only code...
"""

from typing import Dict

from sdk.config.constants import ConstantsBase
from sdk.config.environment import Environment


class ConfigBase:

    def __init__(self, load_config_from_env: bool = True) -> None:
        if load_config_from_env:
            self.reload_config_from_env()

    def reload_config_from_env(
        self, use_dotenv_files: bool = True, default_env: Dict[ConstantsBase.Environment.Variable, str] = None
    ) -> None:
        if default_env is None:
            default_env = ConstantsBase.Environment.default_env()

        self._active_environment = Environment(set_from_dotenv=use_dotenv_files, default_env=default_env)

    @property
    def active_env(self) -> Environment:
        """Gets the active environment object.

        Returns:
            Environment: The active environment object.
        """

        return self._active_environment

    def override_active_environment(self, new_active_environment: Environment) -> None:
        """Override the active environment with a new one.

        Args:
            new_active_environment (Environment): New active environment object.
        """

        self._active_environment = new_active_environment

    def is_development_env(self) -> bool:
        """Checks if the active environment is development.

        Returns:
            bool: True if it is, False otherwise.
        """

        return self.active_env.name == ConstantsBase.Environment.Type.DEVELOPMENT.name

    def is_staging_env(self) -> bool:
        """Checks if the active environment is staging.

        Returns:
            bool: True if it is, False otherwise.
        """

        return self.active_env.name == ConstantsBase.Environment.Type.STAGING.name

    def is_production_env(self) -> bool:
        """Checks if the active environment is production.

        Returns:
            bool: True if it is, False otherwise.
        """

        return self.active_env.name == ConstantsBase.Environment.Type.PRODUCTION.name
