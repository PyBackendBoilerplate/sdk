from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type, TypeVar, Union

from sdk.config.constants import ConstantsBase
from sdk.config.environment import Environment
from sdk.infra.events import notify
from sdk.infra.events.hooks import AppCreationDoneHook

Flask = TypeVar('Flask')
FlaskApp = TypeVar('FlaskApp')  # Connexion app


@dataclass
class MicroserviceSettings:
    name: str = ConstantsBase.Environment.default_env()[ConstantsBase.Environment.Variable.MICROSERVICE_NAME]
    port: int = int(ConstantsBase.Environment.default_env()[ConstantsBase.Environment.Variable.PORT])
    host: str = ConstantsBase.Environment.default_env()[ConstantsBase.Environment.Variable.HOST]

    # def __setattr__(self, name: str, value: Any) -> None:
    #     """ Make read-only when all fields are None"""

    #     # Allow setting an attributes only if all fiels are None (default)
    #     if None not in [getattr(self, field.name) for field in fields(self)]:
    #         raise AttributeError(f'Can\'t set "{value}" for {self.__class__.__name__}.{name} (read-only).')

    #     super().__setattr__(name, value)

    @classmethod
    @abstractmethod
    def build_from_env(cls, env: Environment) -> Type[MicroserviceSettings]:
        cls._update_env(env)
        return cls(name=env.microservice_name, port=env.port, host=env.host)

    @classmethod
    @abstractmethod
    def _update_env(cls, env: Environment) -> None:
        """
        Updates the environment according to the class defaults if not set before

        Args:
            env (Environment): [description]
        """

        host = env.getenv('host')

        if host is None:
            if cls.host is not None:
                env.setenv('host', cls.host)


class Microservice(ABC):

    def __init__(self, settings: Type[MicroserviceSettings]) -> None:
        self._app = None
        self._settings = settings

    @abstractmethod
    def create_app(self) -> Union[Flask, FlaskApp]:
        notify(lambda: AppCreationDoneHook())

        return self.app

    @property
    def settings(self) -> Type[MicroserviceSettings]:
        return self._settings

    @property
    def app(self) -> Union[Flask, FlaskApp]:
        return self._app

    def run(self, *args, **kwargs) -> None:
        self.app.run(args, kwargs)
