import os

from scapy.all import *

os.getenv("IFACE")

threshold = 10

sniff(iface="lo", filter="icmp", store=False, prn=lambda x: print(x))
