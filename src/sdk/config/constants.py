"""The common global constants.

Use the class Constants to access global constants values.
"""

from __future__ import annotations

from enum import Enum, auto, unique
from typing import Dict


class ConstantsBase:
    """
    Extend with local constants like this:
    
    class Constants(ConstantsBase):

    @unique
    class MyConstantsGroup(Enum):
        CONST_A = auto()
        CONST_B = auto()
    """

    class Environment:

        @unique
        class Variable(Enum):

            VSCODE_DEBUG_MODE = auto()
            ACTIVE_ENV = auto()
            MICROSERVICE_NAME = auto()
            PORT = auto()
            HOST = auto()

        @staticmethod
        def default_env() -> Dict[Type[ConstantsBase.Environment.Variable], str]:
            return {
                ConstantsBase.Environment.Variable.VSCODE_DEBUG_MODE: 'False',
                ConstantsBase.Environment.Variable.ACTIVE_ENV: ConstantsBase.Environment.Type.DEVELOPMENT.name,
                ConstantsBase.Environment.Variable.MICROSERVICE_NAME: 'Default Microservice Name',
                ConstantsBase.Environment.Variable.PORT: '5000',
                ConstantsBase.Environment.Variable.HOST: '0.0.0.0'
            }

        @unique
        class Type(Enum):
            DEVELOPMENT = auto()
            STAGING = auto()
            PRODUCTION = auto()

    class Microservice:

        @unique
        class Framework(Enum):
            FLASK = auto()
            CONNEXION = auto()
