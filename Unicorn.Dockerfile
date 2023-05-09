# Kali Linux latest
FROM kalilinux/kali-rolling

# Update
RUN apt -y update && DEBIAN_FRONTEND=noninteractive apt -y dist-upgrade && apt -y autoremove && apt clean

# Install dependencies
RUN DEBIAN_FRONTEND=noninteractive apt -y install python3-pip iproute2 aircrack-ng pciutils procps kmod
RUN python3 -m pip install scapy

# Setup env
RUN mkdir /opt/sniff/
COPY *.py /opt/sniff/
RUN chmod +x /opt/sniff/*.py

ENTRYPOINT /bin/sh -c "/usr/bin/python3 /opt/sniff/sniffsniff.py"
