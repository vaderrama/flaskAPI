#! /bin/bash

#actualizamos
sudo apt-get update

# instalamos pip
sudo apt install python3-pip

#instalamos
pip3 install -U -r requirements.txt

# run
cd app

flask run