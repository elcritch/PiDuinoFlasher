#!/bin/sh

# wget https://adafruit.github.io/arduino-board-index/package_adafruit_index.json

sudo apt install -y gcc-avr binutils-avr avr-libc avrdude
sudo apt install -y bison

## ino -- helper utility for building Arduino projects

sudo apt install -y python-pip
sudo pip install ino

sudo apt-get install -y arduino-mk


sudo pip install -r requirements.txt

# ./flasher-install-adafruit-avr.sh
./flasher-install-arduino-ide.sh

