#!/bin/sh

ard-reset-arduino --verbose --caterina ${AVRDEV} && sleep 0.3 && avrdude -v -p atmega32u4 -c avr109 -P ${AVRDEV} -b 57600 -U flash:w:$HEX_FILE:i

