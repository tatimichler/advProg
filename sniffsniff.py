import os
from scapy.all import *
from scapy.layers.dot11 import Dot11

iface = os.getenv("IFACE")
threshold = 10
ap_list = []

def PacketHandler(packet):
    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype == 12:
            print(f"Access Point MAC: {packet.addr2} with SSID: {packet.addr3}\nAttacker MAC: {packet.addr1}")

sniff(iface="wlan0", prn = PacketHandler)
