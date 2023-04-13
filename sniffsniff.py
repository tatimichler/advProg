#!/usr/bin/python3

from scapy.all import *
from scapy.layers.dot11 import Dot11

iface = os.getenv("IFACE")
threshold = 10
ap_list = []

def PacketHandler(packet):
    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype == 12:
            with open("logedi.log", "a+") as file:
                file.write(str({"reciever" : packet.addr1, "source" : packet.addr2, "bssid" : packet.addr3}) + "\n")

sniff(iface="wlan0", prn = PacketHandler, monitor = True, store = True)