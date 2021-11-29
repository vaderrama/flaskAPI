#! /bin/bash

#actualizamos
sudo apt-get update

# instalamos pip
sudo apt install python3-pip

#instalamos flask
sudo apt install python3-flask

#instalamos
pip3 install -r requirements.txt

# run
flask run