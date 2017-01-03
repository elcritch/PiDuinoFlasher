
ard-reset-arduino --verbose --caterina /dev/ttyACM0 && sleep 0.3 && avrdude -C $AVRCONF -v -p atmega32u4 -c avr109 -P /dev/ttyACM0 -b 57600 -U flash:w:$HEX_FILE:i

