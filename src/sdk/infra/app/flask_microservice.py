from abc import abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Type

from flask.app import Flask

from sdk.config.constants import ConstantsBase
from sdk.config.environment import Environment
from sdk.infra.app.microservice import Microservice, MicroserviceSettings


@dataclass
class FlaskMicroserviceSettings(MicroserviceSettings):
    FLASK_ENV: str = ConstantsBase.Environment.default_env()[ConstantsBase.Environment.Variable.ACTIVE_ENV]
    FLASK_APP: str = None
    template_folder: Path = None

    @classmethod
    @abstractmethod
    def build_from_env(
        cls,
        env: Environment,
        # Not available from .env or .flaskenv
        template_folder: Path = None
    ) -> Type[MicroserviceSettings]:

        cls._update_env(env)

        return cls(
            name=env.microservice_name,
            port=env.port,
            host=env.host,
            FLASK_ENV=env.getenv('FLASK_ENV'),
            FLASK_APP=env.getenv('FLASK_APP'),
            template_folder=template_folder if template_folder is not None else cls.template_folder
        )

    @classmethod
    def _update_env(cls, env: Environment) -> None:
        """
        Updates the environment according to the class defaults if not set before

        Args:
            env (Environment): [description]
        """

        super()._update_env(env)

        FLASK_ENV = env.getenv('FLASK_ENV')

        if FLASK_ENV is None:
            if cls.FLASK_ENV is not None:
                env.setenv('FLASK_ENV', cls.FLASK_ENV)

        FLASK_APP = env.getenv('FLASK_APP')

        if FLASK_APP is None:
            if cls.FLASK_APP is not None:
                env.setenv('FLASK_APP', cls.FLASK_APP)


class FlaskMicroservice(Microservice):

    def create_app(self) -> Flask:
        self._app = Flask(self.settings.name, template_folder=self.settings.template_folder)

        return super().create_app()
