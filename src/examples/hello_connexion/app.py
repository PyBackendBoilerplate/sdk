from pathlib import Path
from sdk.infra.app.wsgi import create_connexion_microservice

if __name__ == '__main__':
    microservice, settings = create_connexion_microservice()
    settings.name = 'Hello Connexion'
    settings.openapi_spec = Path('./openapi/openapi.yaml')
    connexion_app = microservice.create_app()
    connexion_app.run(host=settings.host, port=settings.port)
