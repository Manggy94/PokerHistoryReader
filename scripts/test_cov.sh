#!/bin/bash
# Charger le fichier .env
set -o allexport
source .env
set +o allexport
printenv
echo "Testing Covering on Poker History Reader"
python -m pytest --cov=pkrhistoryreader --cov-report html --cov-report term tests/