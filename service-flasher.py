#!/usr/bin/env python

from __future__ import print_function
import serial
import os.path
import argparse
from time import sleep
import time
import pyudev
import subprocess
#import RPi.GPIO as GPIO

import requests
import pytz 
import hashlib
import datetime


parser = argparse.ArgumentParser(description='Reset an Arduino')
parser.add_argument('--no-caterina', action='store_true', default=False, help='Reset a Leonardo, Micro, Robot or LilyPadUSB.')
parser.add_argument('--verbose', action='store_true', help="Watch what's going on on STDERR.")
parser.add_argument('--period', default=0.1, help='Specify the DTR pulse width in seconds.')
parser.add_argument('--avrconf', default="./arduino-1.8.0/hardware/tools/avr/etc/avrdude.conf", help='AVR Conf File')
parser.add_argument('--avrdude', default="./arduino-1.8.0/hardware/tools/avr/bin/avrdude", help='AVR Conf File')
parser.add_argument('--ifttt', default="XXXXXXXXXXX", help='key for ifttt service notifications')
parser.add_argument('firmware', nargs=1, help='Firmware to flash.')
# parser.add_argument('port', nargs=1, help='Serial device e.g. /dev/ttyACM0')
args = parser.parse_args()

def flash_reset(args):
    if not args.no_caterina:
        if args.verbose: print('Forcing reset using 1200bps open/close on port %s' % args.port[0])
        ser = serial.Serial(args.port[0], 57600)
        ser.close()
        ser.open()
        ser.close()
        ser.setBaudrate(1200)
        ser.open()
        ser.close()
        sleep(1)

        while not os.path.exists(args.port[0]):
            if args.verbose: print('Waiting for %s to come back' % args.port[0])
            sleep(1)

        if args.verbose: print('%s has come back after reset' % args.port[0])
    else:
        if args.verbose: print('Setting DTR high on %s for %ss' % (args.port[0],args.period))
        ser = serial.Serial(args.port[0], 115200)
        ser.setDTR(False)
        sleep(args.period)
        ser.setDTR(True)
        ser.close()

def flash_upload(args):
    print("Flashing upload")
    subprocess.call(["%s"%args.avrdude, 
        "-C", "%s"%(args.avrconf), 
        "-v", 
        "-p", "atmega32u4",
        "-c", "avr109",
        "-P", "%s"%(args.port[0]),
        "-b", "57600", 
        "-U", "flash:w:%s:i"%(args.firmware[0]),
    ])

usb_flash_tick = time.time()
flash_count = 1

def tick():
    global usb_flash_tick
    global flash_count
    usb_flash_tick = time.time()
    flash_count += 1

def tock():
    return time.time() - usb_flash_tick 

def do_flash(args):
    if tock() < 5.0:
        print("Post flash delay, ignoring usbport events. ")
        return

    #GPIO.output(LED_PIN, GPIO.LOW)
    sleep(2)
    print("Flashing device: %s"%args.port[0])
    flash_reset(args)
    sleep(0.6)
    flash_upload(args)
    tick()
    post_status("success", args)
    #GPIO.output(LED_PIN, GPIO.HIGH)

def post_status(status, args):

    if not args.ifttt:
       return None
    
    ts = str(datetime.datetime.now(pytz.timezone('US/Pacific')))
    url = "https://maker.ifttt.com/trigger/flasher_run/with/key/%s"%args.ifttt
    print("post url: ", url)
    
    requests.post(url, json={"value1": str(status), "value2": args.firmware_hash, "value3": "count %d, ts: %s"%(flash_count, ts)})

def usb_monitor():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    # monitor.filter_by(subsystem='usb')  # Remove this line to listen for all devices.
    monitor.start()

    tick()
    for device in iter(monitor.poll, None):
        if device.subsystem == "tty" and device.action == "add":
            print("serial device: ", device.sys_name, device, )
            
            args.port = [ "/dev/" + device.sys_name ]
            
            try: 
                do_flash(args)

            except Exception as err:
                print("Err: ", err)
                post_status("error: %s"%(str(err)), args)


# ('usb device: ', Device(u'/sys/devices/platform/soc/3f980000.usb/usb1/1-1/1-1.3/1-1.3:1.0/tty/ttyACM0'), u'add')

LED_PIN = 47

def main():
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(LED_PIN, GPIO.OUT)
    #GPIO.output(LED_PIN, GPIO.HIGH)
    with open(args.firmware[0], 'r') as file:
       firmware_hash = hashlib.md5(file.read().encode('utf-8')).hexdigest()
       args.firmware_hash = firmware_hash

    args.verbose = True
    print("firmware hash: ", args.firmware_hash)
    usb_monitor()

if __name__ == "__main__":
    main()

