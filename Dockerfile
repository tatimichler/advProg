# Kali Linux latest
FROM kalilinux/kali-rolling

# Update
RUN apt -y update && DEBIAN_FRONTEND=noninteractive apt -y dist-upgrade && apt -y autoremove && apt clean

# Install dependencies
RUN DEBIAN_FRONTEND=noninteractive apt -y install aircrack-ng tcpdump iproute2 pciutils kmod