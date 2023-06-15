# Kali Linux latest
FROM kalilinux/kali-rolling

# Update
RUN apt -y update && DEBIAN_FRONTEND=noninteractive apt -y dist-upgrade && apt -y autoremove && apt clean

# Install dependencies
RUN DEBIAN_FRONTEND=noninteractive apt -y install python3-pip iproute2 aircrack-ng pciutils procps kmod curl libcurl4
# Install FileBeat
RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.7.1-arm64.deb
RUN dpkg -i filebeat-8.7.1-amd64.deb
RUN python3 -m pip install scapy
RUN python3 -m pip install python-dotenv

# Setup env
RUN mkdir /opt/sniff/
COPY *.py /opt/sniff/
RUN chmod +x /opt/sniff/*.py

COPY filebeat.yml /etc/filebeat/
COPY fields.yml /usr/share/filebeat/

# For debugging reasons
COPY logedi.log /opt/sniff/

ENTRYPOINT /bin/sh -c "/usr/bin/python3 /opt/sniff/sniffsniff.py"
