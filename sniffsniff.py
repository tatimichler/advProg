from scapy.all import *

sniff(iface="lo", store=False, prn=lambda x : print(x))