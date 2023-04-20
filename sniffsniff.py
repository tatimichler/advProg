#!/usr/bin/python3

from scapy.all import *
from scapy.layers.dot11 import Dot11

iface = os.getenv("IFACE")
threshold = 300
ap_list = ["b8:27:eb:ac:05:0f"]
target_list = {}


def check_for_threshold(recieved_packet):
    if recieved_packet.addr1 in ap_list:
        if not recieved_packet.addr2 in target_list:
            target_list[recieved_packet.addr2] = {"packets": [recieved_packet], "timestamp": [datetime.now().second]}
        else:
            target_list[recieved_packet.addr2]["timestamp"].append(datetime.now().second)
            target_list[recieved_packet.addr2]["packets"].append(recieved_packet)
        if len(target_list[recieved_packet.addr2]["timestamp"]) > threshold and target_list[recieved_packet.addr2]["timestamp"][-1] - [recieved_packet.addr2]["timestamp"][0] <= 1:
            for packet_i in range(len(target_list[recieved_packet.addr2]["packets"])):
                with open("logedi.log", "a+") as file:
                    file.write(str({"timestamp": target_list[recieved_packet.addr2]["timestamps"][packet_i], "reciever": target_list[recieved_packet.addr2]["packets"][packet_i].addr1, "source": target_list[recieved_packet.addr2]["packets"][packet_i].addr2, "bssid": target_list[recieved_packet.addr2]["packets"][packet_i].addr3}) + "\n")


def deauth_detector(recieved_packet):
    if recieved_packet.haslayer(Dot11):
        if recieved_packet.type == 0 and recieved_packet.subtype == 12:
            check_for_threshold(recieved_packet)


sniff(iface="wlan0", prn=deauth_detector, monitor=True, store=True)
