from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Type

import connexion
import prance
from connexion.apps.flask_app import FlaskApp
from connexion.jsonifier import JSONEncoder

from sdk.infra.app.flask_microservice import FlaskMicroserviceSettings
from sdk.infra.app.microservice import Microservice


class PyFlaskBackendJSONEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.name

        return JSONEncoder.default(self, obj)


@dataclass
class ConnexionMicroserviceSettings(FlaskMicroserviceSettings):
    openapi_spec: Path = Path('src/openapi/openapi.yaml')
    strict_validation: bool = True
    validate_responses: bool = True


class ConnexionMicroservice(Microservice):

    def create_app(self) -> FlaskApp:
        self._app = connexion.FlaskApp(
            self.settings.name, port=self.settings.port, specification_dir=self.settings.openapi_spec.parent
        )

        self.set_json_encoder(json_encoder=PyFlaskBackendJSONEncoder)

        self.app.add_api(
            specification=self._get_bundled_specs(self.settings.openapi_spec),
            strict_validation=self.settings.strict_validation,
            validate_responses=self.settings.validate_responses
        )

        return super().create_app()

    def set_json_encoder(self, json_encoder: Type) -> None:
        self.app.appjson_encoder = json_encoder

    def _get_bundled_specs(self, main_file: Path) -> Dict[str, Any]:
        """ https://github.com/zalando/connexion/issues/254#issuecomment-497194240 """

        parser = prance.ResolvingParser(str(main_file.absolute()), lazy=True, backend='openapi-spec-validator')
        parser.parse()

        return parser.specification
