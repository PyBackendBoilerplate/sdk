"""This module handles all environment r/w access.

Use the class Environment to access environment variable and general environment settings.
"""

import os
from pathlib import Path
from typing import Dict, Union

from dotenv import load_dotenv

from sdk.config.constants import ConstantsBase


class Environment:
    """
    Gives access to environment variable and general environment settings.
    """

    def __init__(
        self, set_from_dotenv: bool = True, default_env: Dict[ConstantsBase.Environment.Variable, str] = None
    ) -> None:

        self._default_env = default_env if default_env is not None else dict()

        if set_from_dotenv:
            self.set_from_dotenv(verbose=True)  # TODO: change verbose to False

    def set_from_dotenv(
        self, dotenv_path: Path = Path('.env'), flaskenv=Path('.flaskenv'), verbose: bool = True
    ) -> None:
        """
        Loads .env and .flaskenv files.

        Args:
            dotenv_path (Path, optional): Path to .env file. Defaults to Path('.env').
            verbose (bool, optional): See load_dotenv(). Defaults to True.
        """

        if dotenv_path.exists:
            load_dotenv(dotenv_path=dotenv_path, verbose=verbose)

        if flaskenv.exists:
            load_dotenv(dotenv_path=flaskenv, verbose=verbose)

    @property
    def name(self) -> str:
        """
        Gets the name of the active environment.

        Returns:
            str: One of the possible options from ConstantsBase.Environment.
        """

        return self.getenv(ConstantsBase.Environment.Variable.ACTIVE_ENV)

    @property
    def microservice_name(self) -> str:
        """
        Gets the name of the microservice.

        Returns:
            str: The name of the microservice.
        """

        return self.getenv(ConstantsBase.Environment.Variable.MICROSERVICE_NAME)

    @property
    def port(self) -> int:
        """
        Gets the port of the microservice.

        Returns:
            int: The flask app port.
        """

        return int(self.getenv(ConstantsBase.Environment.Variable.PORT))

    @property
    def host(self) -> str:
        """
        Gets the host of the microservice.

        Returns:
            str: The flask app host.
        """

        # The hosts needs to be treated as lowercase because Flask requires
        # it to be in the .flaskenv and we want to keep consistency so we lower() it too
        return self.getenv(ConstantsBase.Environment.Variable.HOST.name.lower())

    @property
    def vscode_debug_mode(self) -> bool:
        """
        Gets the debug mode relevant for vscode debugging.
        Possible values: True/False, 1/0, On/Off.

        Returns:
            bool: True if debug mode is one, False otherwise.
        """

        vscode_debug_mode = self.getenv(ConstantsBase.Environment.Variable.VSCODE_DEBUG_MODE)

        return vscode_debug_mode.lower() in ['true', 'on', '1']

    def getenv(self, key: Union[ConstantsBase.Environment.Variable, str]) -> Union[str, None]:
        """
        Wrapper for os.getenv() that applies custom defaults.

        Args:
            key (Union[ConstantsBase.Environment.Variable, str]): The environment variable to fetch.

        Returns:
            Union[str, None]: The environment variable value / default value / None if N/A.
        """

        # Try to get the env var

        if isinstance(key, ConstantsBase.Environment.Variable):
            env_var = os.getenv(key.name, None)
        else:
            env_var = os.getenv(key, None)

        # If nothing was found

        if env_var is None:

            # And the env var has a predefined default

            if isinstance(key, ConstantsBase.Environment.Variable):
                if key in self._default_env:

                    # Return the default value and sets it back into the environment

                    env_var = self._default_env[key]
                    self.setenv(key, env_var)

        return env_var

    def setenv(self, key: Union[ConstantsBase.Environment.Variable, str], value: str) -> None:
        """
        Sets a new environment variable in os.environ.

        Args:
            key (Union[ConstantsBase.Environment.Variable, str]): The environment variable key.
            value (str): The environment variable string value.
        """

        if isinstance(key, ConstantsBase.Environment.Variable):
            os.environ[key.name] = str(value)
        else:
            os.environ[key] = str(value)
