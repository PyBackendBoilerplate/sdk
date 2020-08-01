from typing import Type
from sdk.config import ConfigBase
from sdk.config.constants import ConstantsBase
from sdk.infra.app.connexion_microservice import ConnexionMicroservice, ConnexionMicroserviceSettings
from sdk.infra.app.flask_microservice import FlaskMicroservice, FlaskMicroserviceSettings
from sdk.infra.app.microservice import Microservice, MicroserviceSettings
from sdk.infra.events.handlers import register_infra_events_handlers
from sdk.utilities.vscode import initialize_flask_server_debugger_if_needed

initialize_flask_server_debugger_if_needed()


def create_microservice(
    framework_type: ConstantsBase.Microservice.Framework,
    build_from_env: bool = True,
    build_from_settings: Type[MicroserviceSettings] = None
) -> Type[Microservice]:
    """
    Creates the microservice object.

    Args:
        framework_type (ConstantsBase.Microservice.Framework): [description]
        build_from_env (bool, optional): [description]. Defaults to True.
        build_from_settings (Type[MicroserviceSettings], optional): [description]. Defaults to None.

    Returns:
        Type[Microservice]: Microservice object.
    """

    register_infra_events_handlers()

    microservice = None
    settings = build_from_settings
    env = ConfigBase().active_env

    if framework_type == ConstantsBase.Microservice.Framework.FLASK:
        if build_from_env:
            settings = FlaskMicroserviceSettings.build_from_env(env)
        microservice = FlaskMicroservice(settings)

    if framework_type == ConstantsBase.Microservice.Framework.CONNEXION:
        if build_from_env:
            settings = ConnexionMicroserviceSettings.build_from_env(env)
        microservice = ConnexionMicroservice(settings)

    return microservice
