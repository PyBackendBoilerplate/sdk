# PyBackendBoilerplate Software Development Kit (SDK)

## Development status: WIP

This package encapsulate all of the common infrastructure required to implement a [Flask](https://flask.palletsprojects.com/) based [microservice](https://github.com/PyBackendBoilerplate/micro-service) with support for [OpenAPI 3](https://swagger.io/specification/) and [Connexion](https://github.com/zalando/connexion) out-of-the-box.

## Tech Stack

The package is tested on Python 3.8, but Python 3.7 should also work (minimum version though).

The following list describes part of the stack used in the SDK:
* **[Flask](https://flask.palletsprojects.com/)**: Web Framework.
* **[Connexion](https://github.com/zalando/connexion)**: OpenAPI Framework.
* **[Gunicorn](https://gunicorn.org/)**: Python WSGI HTTP Server.
* **[zope.event](https://zopeevent.readthedocs.io/)**: Events framework.

### Configurations

The SDK also supports loading configurations from the following options:
* [defaults](./src/sdk/config/constants.py#L36)
* .env
* .flaskenv
* [gunicorn_conf.py](./src/sdk/config/gunicorn_conf.py)

By default, it will first try to load the `.env` and `.flaskenv` files.
If N/A, it will use the [defaults](./src/sdk/config/constants.py#L36) defined in the code (Notice: There aren't defaults for everything, just the minimum required to run on host and port per defined in the defaults).

To access these values, use [`class ConfigBase`](./src/sdk/config/__init__.py#L19) and [`class Environment`](./src/sdk/config/environment.py#L15), e.g:
```
# This will automatically try to load the environment configurations 
# and return a built Environment object.
env: Environment = ConfigBase().active_env
```

#### Gunicorn

When running with [gunicorn](https://gunicorn.org/), you can use defaults from the [src/sdk/config/gunicorn_conf.py](./src/sdk/config/gunicorn_conf.py).
To override them, just create your own `gunicorn_conf.py` file like this and use that when running gunicorn:
```
import sys
import os

sys.path.append(os.path.join(sys.path[0], 'src'))
from sdk.config.gunicorn_conf import *

# override default sdk values here

bind = '0.0.0.0:5555'
```

## Examples

The SDK comes with built-in examples under [src/examples](./src/examples) which shows how to use the SDK to build the official examples of Flask and Connexion with the SDK's infrastructure.

## Development

The SDK is developed in [VS Code](https://code.visualstudio.com/) and provides a [.vscode](./.vscode) directory with predefined settings to get your VS Code environment ready fast.

### Coding Style

The coding style format is according to [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

The coding style is automatically formatted with [yapf](https://github.com/google/yapf) and configured for [Google coding style](./.style.yapf#L7) by default.
To see the full configurations, check the [.style.yapf](./.style.yapf) configuration file.

The documentation is also configured via the provided [.vscode settings](./.vscode) to [Google coding style](./.vscode/settings.json#L9) by default.

## References

Thanks sections for projects which helped me develop this one:
* https://github.com/dgarcia360/openapi-boilerplate
* https://github.com/adriencaccia/vscode-flask-debug
* https://github.com/Humanitec/blueprint_flask_service