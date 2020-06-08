#!/usr/bin/env python3

from boofuzz import *

# target info
host = "192.168.145.128"
port = 9999

# boilerplate boofuzz stuff

session = Session(target=Target(connection=SocketConnection(host, port, proto="tcp")))

# create a mode

s_initialize("HTER")

# specify how the fuzz syntax works
s_string("HTER" , fuzzable=False)
s_delim(" ", fuzzable=False)
s_string("FUZZ") # this is our fuzz point

# connected to the service
session.connect(s_get("HTER"))
session.fuzz()