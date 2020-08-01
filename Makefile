# Taken from: https://github.com/adriencaccia/vscode-flask-debug

.PHONY: help
.DEFAULT_GOAL := help
help:
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'


## Build tools
clean:   ## Clean __pycache__ files.
	py3clean .


## Start the examples
hello_connexion:  ## src/examples/hello_connexion.
	./run_example.sh hello_connexion

hello_flask:  ## src/examples/hello_flask.
	./run_example.sh hello_flask