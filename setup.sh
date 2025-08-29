#!/bin/bash

mkdir instance/
cp app/.setup_templates/base_debug_config.py instance/local_config.py
flask setup-db

mkdir -p app/static/uploaded/gallery
