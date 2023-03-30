# advProg
Repository for Advanced Programming Project

Super Sache hier! ^v^

Ja finde ich auch :3 

# Build image
`docker build -t pinkfluffyunicorn:dev .`

# Start image
`docker run --privileged -it --network host pinkfluffyunicorn:dev /bin/bash`

# Aufräumen
Alle container zeigen

`docker ps`

Alle images zeigen 

`docker images`

Bestimmte images löschen 
(hashes durch docker images suchen)

`docker rmi imagehash1 imagehash2 imagehash3`
