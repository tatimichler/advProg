# Kali Linux latest
FROM kalilinux/kali-rolling

# Update
RUN apt -y update && DEBIAN_FRONTEND=noninteractive apt -y dist-upgrade && apt -y autoremove && apt clean

# Install dependencies
RUN DEBIAN_FRONTEND=noninteractive apt -y install python3-pip
RUN python3 -m pip install scapy

# Setup env
RUN mkdir /opt/sniff/
COPY *.py /opt/sniff/