#!/bin/sh

# wget https://adafruit.github.io/arduino-board-index/package_adafruit_index.json

sudo apt install -y gcc-avr binutils-avr avr-libc avrdude

## ino -- helper utility for building Arduino projects

sudo apt install -y python-pip
sudo pip install ino

sudo apt-get install -y arduino-mk


wget https://adafruit.github.io/arduino-board-index/boards/adafruit-avr-1.4.9.tar.bz2

echo '2fbc90df3cc0b95816ac39da262ddb6eac5c46e47374768bd7de7c99fac1f3dd adafruit-avr-1.4.9.tar.bz2' | sha256sum -c -

