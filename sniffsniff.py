#!/usr/bin/python3

from uuid import uuid4

from scapy.all import *
from scapy.layers.dot11 import Dot11


class Sniffer():
    def __init__(self, iface=os.getenv("IFACE"), threshold=250, ap_list=["d4:3f:cb:91:4c:46"], target_queue=[None],
                 attack_uuid=None, time_delta=1.0):
        self.iface = iface
        self.threshold = threshold
        self.ap_list = ap_list
        self.target_queue = target_queue * self.threshold
        self.attack_uuid = attack_uuid
        self.time_delta = time_delta

    def write_packet_to_file(self, buffer_item: dict):
        with open("logedi.log", "a+") as outfile:
            outfile.write(str({"timestamp": buffer_item["packet"].time, "reciever": buffer_item["packet"].addr1,"source": buffer_item["packet"].addr2, "bssid": buffer_item["packet"].addr3,"attack_uuid": buffer_item["attack_uuid"]}) + "\n")

    def check_for_threshold(self, recieved_packet):
        if recieved_packet.addr1.lower() in self.ap_list:
            print("Test 1")
            if not self.target_queue[0]:  # if buffer not full
                print("Test 2")
                # dequeue + enqueue
                # buffer not full (startup)
                self.target_queue.pop(0)
                self.target_queue.append({"packet": recieved_packet, "attack_uuid": self.attack_uuid})
            elif self.target_queue[0] and recieved_packet.time - self.target_queue[0][
                "packet"].time <= self.time_delta and self.attack_uuid:  # if buffer full AND time_delta met AND there is an ongoing attack
                print("Test 3")
                # dequeue + enqueue + write new packet to file
                # still ongoing attack
                self.target_queue.pop(0)
                self.target_queue.append({"packet": recieved_packet, "attack_uuid": self.attack_uuid})
                self.write_packet_to_file(self.target_queue[-1])
            elif self.target_queue[0] and recieved_packet.time - self.target_queue[0]["packet"].time <= self.time_delta and not self.attack_uuid:  # if buffer full AND time_delta met AND there is no ongoing attack
                print("Test 4")
                # create new attack ID + check if oldest packet has no attack ID -> add attack ID to all packets in buffer and write them to file else dequeue + enqueue + write new packet to file
                # new attack
                self.attack_uuid = uuid4()
                for buffer_item in self.target_queue:
                    if not buffer_item["attack_uuid"]:
                        buffer_item["attack_uuid"] = self.attack_uuid
                        self.write_packet_to_file(buffer_item)
                self.target_queue.pop(0)
                self.target_queue.append({"packet": recieved_packet, "attack_uuid": self.attack_uuid})
                self.write_packet_to_file({"packet": recieved_packet, "attack_uuid": self.attack_uuid})
            elif self.target_queue[0] and recieved_packet.time - self.target_queue[0]["packet"].time > self.time_delta and self.attack_uuid:  # if buffer full AND time_delta NOT met AND there is no ongoing attack
                print("Test 5")
                # set attack ID to none (no attack) + dequeue + enqueue
                # no malicious packets anymore
                self.attack_uuid = None
                self.target_queue.pop(0)
                self.target_queue.append({"packet": recieved_packet, "attack_uuid": self.attack_uuid})
            elif self.target_queue[0] and recieved_packet.time - self.target_queue[0]["packet"].time > self.time_delta and not self.attack_uuid:  # if buffer full AND time_delta NOT met AND there is no ongoing attack
                print("Test 6")
                # dequeue + enqueue
                # no malicious packets
                self.target_queue.pop(0)
                self.target_queue.append({"packet": recieved_packet, "attack_uuid": self.attack_uuid})

    def deauth_detector(self, recieved_packet):
        if recieved_packet.haslayer(Dot11):
            if recieved_packet.type == 0 and recieved_packet.subtype == 12:
                self.check_for_threshold(recieved_packet)


if __name__ == "__main__":
    sniffler = Sniffer()
    sniff(iface="wlan0", prn=sniffler.deauth_detector, monitor=True, store=True)
