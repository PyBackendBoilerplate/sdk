#!/bin/bash

# TODO: Add doc

if [ -f .env ]; then
    # Export the vars in .env into your shell:
    export $(egrep -v '^#' .env | xargs)
fi

if [[ -z "${ACTIVE_ENV}" ]]; then
  ACTIVE_ENV="DEVELOPMENT"
else
  ACTIVE_ENV="${ACTIVE_ENV}"
fi

echo "Active Environment: $ACTIVE_ENV"

VENV=".venv"

if [ -d "$VENV" ]; then
    echo "Installing pip requirements files in the virtual environment: $VENV"
    source .venv/bin/activate
else
    echo "Installing pip requirements files in the default python installation"
fi

echo

pip install --upgrade pip

if [ $ACTIVE_ENV = 'DEVELOPMENT' ]; then
    pip install -r requirements/development.txt
elif [ $ACTIVE_ENV = 'STAGING' ]; then
    pip install -r requirements/staging.txt
elif [ $ACTIVE_ENV = 'PRODUCTION' ]; then
    pip install -r requirements/production.txt
fi

if [ -d "$VENV" ]; then
    deactivate
    echo
    echo "Finished installing pip requirements files in the virtual environment: $VENV"
else
    echo "Finished installing pip requirements files in the default python installation"
fi
