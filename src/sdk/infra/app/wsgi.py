from typing import Tuple, Type

from sdk.config.constants import ConstantsBase
from sdk.infra.app import create_microservice
from sdk.infra.app.connexion_microservice import ConnexionMicroservice
from sdk.infra.app.flask_microservice import FlaskMicroserviceSettings
from sdk.infra.app.microservice import MicroserviceSettings


def create_flask_microservice() -> Tuple[FlaskMicroserviceSettings, Type[MicroserviceSettings]]:
    microservice = create_microservice(ConstantsBase.Microservice.Framework.FLASK)
    return microservice, microservice.settings


def create_connexion_microservice() -> Tuple[ConnexionMicroservice, Type[MicroserviceSettings]]:
    microservice = create_microservice(ConstantsBase.Microservice.Framework.CONNEXION)
    return microservice, microservice.settings
