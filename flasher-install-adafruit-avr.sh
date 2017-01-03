#!/bin/sh

wget https://adafruit.github.io/arduino-board-index/boards/adafruit-avr-1.4.9.tar.bz2

echo '2fbc90df3cc0b95816ac39da262ddb6eac5c46e47374768bd7de7c99fac1f3dd adafruit-avr-1.4.9.tar.bz2' | sha256sum -c -

tar jxvf adafruit-avr-1.4.9.tar.bz2

mv adafruit-avr-1.4.9/ /usr/share/arduino/hardware/adafruit-avr

