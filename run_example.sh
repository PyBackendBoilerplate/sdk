#!/bin/bash

VENV=".venv"
if [ ! -d "$VENV" ]; then
    echo "Installing virtual environment in $VENV"
    python3 -m venv $VENV

    ./install_requirements.sh
fi

run_example(){
    MICROSERVICE_DIR="src/examples/${1}"
    cd $MICROSERVICE_DIR
    echo "Running $MICROSERVICE_DIR/app.py"
    python app.py
}

source .venv/bin/activate

run_example $1

deactivate

py3clean .