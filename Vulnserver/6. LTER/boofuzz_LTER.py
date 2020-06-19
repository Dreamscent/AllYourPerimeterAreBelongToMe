#!/usr/bin/python3

from boofuzz import *

host = '192.168.145.129'  # Target IP
port = 9999  # Target Port
proto = 'tcp'

def main():

    session = Session(target=Target(
        connection=SocketConnection(host, port, proto=proto)))

    s_initialize("LTER")  # just giving our session a name, "LTER"

    # these strings are fuzzable by default, so here instead of blank, we specify 'false'
    s_string("LTER", fuzzable=False)

    # we don't want to fuzz the space between "TRUN" and our arg
    s_delim(" ", fuzzable=False)

    # This value is arbitrary as we did not specify 'False' for fuzzable. Boofuzz will fuzz this string now
    s_string("FUZZ")

    # having our 'session' variable connect following the guidelines we established in "TRUN"
    session.connect(s_get("LTER"))
    session.fuzz()  # calling this function actually performs the fuzzing


if __name__ == "__main__":
    main()
