#!/bin/bash

source env/bin/activate
pip install -r requirements

export FLASK_ENV=development
export FLASK_APP=src/main.py

flask run
