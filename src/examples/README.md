# SDK Examples

The SDK comes with a few examples that shows the most basic usage.
The examples code can be found under [src/examples/]() and can be ran using the [make](https://linux.die.net/man/1/make) command for easy auto-completion.

Run `make help` for more info.

Lastly, have the `cwd` be the project's root folder for everything to work smoothly (but you can still run it from the `app.py`'s base directory, don't worry).

## Hello Flask

This example project shows how to use the SDK to create the minimal [Flask](https://flask.palletsprojects.com/) application, implementing the official examples for [a minimal app](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) and [rendering templates](https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates).

### Project structure

```
hello_flask
│   app.py -> All of the app's source code
|   sdk -> Soft link to ../../sdk/
│
└───templates
│   │   hello.html -> Taken from Flaks's quickstart page
```

### How to run

1. Clone the full sdk repository.
2. Change dir into the sdk root folder.
3. Run `make hello_flask` (Notice: auto-completion works here...).

If all done correctly, you should see something like this:
```
(.venv) username@ [~/PyBackendBoilerplate/sdk]:
$ make hello_flask
<virtual environment installation log>
./run_example.sh hello_flask
Running src/examples/hello_flask/app.py
 * Serving Flask app "Hello Flask" (lazy loading)
 * Environment: DEVELOPMENT
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

And then the following routes should work locally, as defined in [src/examples/hello_flask/app.py](./hello_flask/app.py#L13):
* http://localhost:5000/
* http://localhost:5000/hello/
* http://localhost:5000/hello/dave/

## Hello Connexion

This example project shows how to use the SDK to create a [Connexion](https://github.com/zalando/connexion) app.
This examples uses [OpenAPI 3](https://swagger.io/specification/) (in junction with [prance](https://github.com/jfinkhaeuser/prance) to split the YAML files), and implements two RESTful APIs (routes), one that is [implemented in the example app itself](./hello_connexion/api/root.py) and one that uses a [predefined route implementation](../sdk/api/common/ping.py) from the SDK itself.

### Project structure

```
hello_connexion
│   app.py -> App's entry code (main)
|   sdk -> Soft link to ../../sdk/
│
└───api -> All routes RESTful APIs implementation
│   │   root.py -> Implements the root path's RESTful API
│   
└───openapi -> Root folder for the OpenAPI specification YAML files
    │   openapi.yaml -> Main (root) OpenAPI specification YAML file
│   │
│   └───paths -> YAML files for specific RESTful APIs (routes) definitions
│       │   ping.yaml -> Definition for the /ping RESTful API, implementing using the SDK's predefined API implementation
```

### How to run

1. Clone the full sdk repository.
2. Change dir into the sdk root folder.
3. Run `make hello_connexion` (Notice: auto-completion works here...).

If all done correctly, you should see something like this:
```
(.venv) username@ [~/PyBackendBoilerplate/sdk]:
$ make hello_connexion
<virtual environment installation log>
./run_example.sh hello_connexion
Running src/examples/hello_connexion/app.py
 * Serving Flask app "Hello Connexion" (lazy loading)
 * Environment: DEVELOPMENT
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

And then the following routes should work locally, as defined in [src/examples/hello_connexion/openapi/openapi.yaml](./hello_connexion/openapi/openapi.yaml#L9):
* http://localhost:5000/
* http://localhost:5000/ping/

In addition, the SDK configures connexion to automatically generate a Swagger UI route, like this (which should show both of the above RESTful APIs (routes)):
* http://localhost:5000/ui/#/