# Kali Linux latest
FROM kalilinux/kali-rolling

# Update
RUN apt -y update && DEBIAN_FRONTEND=noninteractive apt -y dist-upgrade && apt -y autoremove && apt clean

# Install dependencies
RUN DEBIAN_FRONTEND=noninteractive apt -y install python3-pip iproute2 aircrack-ng pciutils procps kmod curl libcurl3
# Install FileBeat
RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.7.1-amd64.deb
RUN sudo dpkg -i filebeat-8.7.1-amd64.deb
RUN python3 -m pip install scapy
RUN python3 -m pip install python-dotenv

# Setup env
RUN mkdir /opt/sniff/
COPY *.py /opt/sniff/
RUN chmod +x /opt/sniff/*.py

ENTRYPOINT /bin/sh -c "/usr/bin/python3 /opt/sniff/sniffsniff.py"
