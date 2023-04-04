# Eingesetzte Technologien
- Pi-Sniff > Python-Skript (Scapy)
- Pi-Schick > Python-Skript | Filebeat
- Server-DB > Elasticsearch | MongoDB
- Server-GUI > Kibana | Grafana | Selber basteln(?)

# Python
## Install requirements
`pip install -r requirements.txt`

## Run
Skript muss mit `sudo` ausgeführt werden, um auf NIC zugreifen zu können.

# Docker
## Build image
`docker build -t pinkfluffyunicorn:dev -f "$(pwd)/Kali.Dockerfile" .`

## Start image
`docker run --privileged -it --network host pinkfluffyunicorn:dev /bin/bash`

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

# Docker Compose (wenn Image gebuildet wurde)

## .env

Beinhaltet Environment-Daten für das Docker-Compose-Skript.

## Run

`docker compose up -d`

## Attach

`docker attach <name>`
