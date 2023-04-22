#!/usr/bin/python3

from uuid import uuid4

from scapy.all import *
from scapy.layers.dot11 import Dot11


class Sniffer():
    def __init__(self, iface=os.getenv("IFACE"), threshold=250, time_delta=1.0, ap_list=["d4:3f:cb:91:4c:46"],
                 target_queue=[None], attack_uuid=None):
        """
        Constructor of deauth attack sniffer.

        :param iface: Tapped interface
        :param threshold: frame threshold
        :param time_delta: Time threshold
        :param ap_list: List of APs to get monitored
        :param target_queue: Queue of received possible attack frames
        :param attack_uuid: UUID of current attack
        """

        self.iface = iface
        self.threshold = threshold
        self.time_delta = time_delta
        self.ap_list = ap_list
        self.target_queue = target_queue * self.threshold
        self.attack_uuid = attack_uuid

    def write_frame_to_file(self, buffer_item: dict):
        """
        Write a given item of the frame buffer to the log file.
        The file will have the JSON form {"timestamp" : timestamp, "receiver" : receiver_mac, "source" : source_mac,
        "bssid" : bssid_mac, "attack_uuid" : attack_uuid}. Where receiver, source and bssid are the partial spoofed
        MAC-addresses chosen by the attacker.

        :param buffer_item: Item of frame buffer in form of {"frame" : received_frame, "attack_uuid" :
        currenct_attacK_uuid}
        """
        with open("logedi.log", "a+") as outfile:
            outfile.write(str({"timestamp": buffer_item["frame"].time, "reciever": buffer_item["frame"].addr1,
                               "source": buffer_item["frame"].addr2, "bssid": buffer_item["frame"].addr3,
                               "attack_uuid": buffer_item["attack_uuid"]}) + "\n")

    def check_for_threshold(self, recieved_frame):
        """
        Use the received frame to check, if it is part of a running attack.
        Will be done by comparison of timestamps of oldest and current frame. Then pop oldest and push current
        frame in FIFO-queue. If current frame is part of attack write it to log file. For each attack a new random
        UUID will be created.

        :param recieved_frame: The current received frame.
        """
        if recieved_frame.addr1.lower() in self.ap_list:
            print("Test 1")
            if not self.target_queue[0]:  # if buffer not full
                print("Test 2")
                # dequeue + enqueue
                # buffer not full (startup)
                self.target_queue.pop(0)
                self.target_queue.append({"frame": recieved_frame, "attack_uuid": self.attack_uuid})
            elif self.target_queue[0] and recieved_frame.time - self.target_queue[0][
                "frame"].time <= self.time_delta and self.attack_uuid:  # if buffer full AND time_delta met AND there is an ongoing attack
                print("Test 3")
                # dequeue + enqueue + write new frame to file
                # still ongoing attack
                self.target_queue.pop(0)
                self.target_queue.append({"frame": recieved_frame, "attack_uuid": self.attack_uuid})
                self.write_frame_to_file(self.target_queue[-1])
            elif self.target_queue[0] and recieved_frame.time - self.target_queue[0][
                "frame"].time <= self.time_delta and not self.attack_uuid:  # if buffer full AND time_delta met AND there is no ongoing attack
                print("Test 4")
                # create new attack ID + check if oldest frame has no attack ID -> add attack ID to all frames in buffer and write them to file else dequeue + enqueue + write new frame to file
                # new attack
                self.attack_uuid = uuid4()
                for buffer_item in self.target_queue:
                    if not buffer_item["attack_uuid"]:
                        buffer_item["attack_uuid"] = self.attack_uuid
                        self.write_frame_to_file(buffer_item)
                self.target_queue.pop(0)
                self.target_queue.append({"frame": recieved_frame, "attack_uuid": self.attack_uuid})
                self.write_frame_to_file({"frame": recieved_frame, "attack_uuid": self.attack_uuid})
            elif self.target_queue[0] and recieved_frame.time - self.target_queue[0][
                "frame"].time > self.time_delta and self.attack_uuid:  # if buffer full AND time_delta NOT met AND there is no ongoing attack
                print("Test 5")
                # set attack ID to none (no attack) + dequeue + enqueue
                # no malicious frames anymore
                self.attack_uuid = None
                self.target_queue.pop(0)
                self.target_queue.append({"frame": recieved_frame, "attack_uuid": self.attack_uuid})
            elif self.target_queue[0] and recieved_frame.time - self.target_queue[0][
                "frame"].time > self.time_delta and not self.attack_uuid:  # if buffer full AND time_delta NOT met AND there is no ongoing attack
                print("Test 6")
                # dequeue + enqueue
                # no malicious frames
                self.target_queue.pop(0)
                self.target_queue.append({"frame": recieved_frame, "attack_uuid": self.attack_uuid})

    def deauth_detector(self, recieved_frame):
        """
        Check if the current received frame is a deauthentication management frame, depending on type and subtype of frame.

        :param recieved_frame: The current received frame
        """
        if recieved_frame.haslayer(Dot11):
            if recieved_frame.type == 0 and recieved_frame.subtype == 12:
                self.check_for_threshold(recieved_frame)


if __name__ == "__main__":
    sniffler = Sniffer()
    sniff(iface="wlan0", prn=sniffler.deauth_detector, monitor=True, store=True)
