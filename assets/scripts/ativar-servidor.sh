#!/bin/bash

cd ../../
python3 -m venv venv
source venv/bin/activate
cd djangoroot
pip install -r requirements.txt
python3 manage.py runserver