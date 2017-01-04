# PiDuinoFlasher

Downloading:

```
sudo su
cd /root/
apt-get install -y git
git clone https://github.com/elcritch/PiDuinoFlasher.git
```

Setup:

```
sudo su
cd /root/PiDuinoFlasher/
sh ./flasher-setup.sh 
sh ./flasher-install-adafruit-avr.sh
sh ./flasher-crontab.sh
reboot
```

