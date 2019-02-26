#! /bin/bash
sudo apt-get install -y mosquitto mosquitto-clients
sudo apt-get install -y python3 
sudo apt-get install -y python3-pip
pip3 install --upgrade pip
pip3 install paho-mqtt
sudo /etc/init.d/mosquitto stop
sudo cp mosquitto.conf /etc/mosquitto/conf.d
sudo /etc/init.d/mosquitto start
