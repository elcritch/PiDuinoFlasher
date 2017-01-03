
# wget https://adafruit.github.io/arduino-board-index/package_adafruit_index.json

sudo apt install -y gcc-avr binutils-avr avr-libc avrdude

## ino -- helper utility for building Arduino projects

sudo apt install -y python-pip
sudo pip install ino

sudo apt-get install arduino-mk


## Working command:
ard-reset-arduino --verbose --caterina /dev/ttyACM0 && sleep 0.3 && avrdude -C ./avrdude.conf -v -p atmega32u4 -c avr109 -P /dev/ttyACM0 -b 57600 -U flash:w:$HEX_FILE:i

