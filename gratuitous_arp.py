#!/usr/bin/env/python3

from scapy.all import *

E = Ether()
E.src = “”
E.dst = “”

A = ARP()
A.op = 1
A.hwsrc = “”
A.psrc  = “”
A.hwdst = “”
A.pdst  = “”

print(“Sending the following packet\n”)
p = E/A
p.show()
sendp(p)
