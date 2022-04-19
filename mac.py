#!/usr/bin/env python

import subprocess
import argparse
import re


def commands(interface, mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])
    #subprocess.call("ifconfig")


def argms():
    args = argparse.ArgumentParser()
    args.add_argument("-i", "--interface", dest="interphase", help="Enter Interphase", metavar=".")
    args.add_argument("-m", "--mac", dest="mac", help="Enter mac")
    option= args.parse_args()
    if not option.interphase:
        args.error("Enter the interface")
    elif not option.mac:
        args.error("enter the mac")
    else:
        return option


def check(interface):
    mac_address = subprocess.check_output(["ifconfig", interface])
    mac_check = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', mac_address)
    if mac_check:
        return mac_check.group(0)
    else:
        print("No mac addresss found")


option1 = argms()
print("mac address is: "+str(check(option1.interphase)))
commands(option1.interphase, option1.mac)

if check(option1.interphase) == option1.mac:
    print("mac address is: "+str(check(option1.interphase)))
else:
    print("mac address cant changed")