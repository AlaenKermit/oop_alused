from klass import *
# Teeme kolme kasutaja eksemplaarid
kasutaja1 = Kasutaja()
kasutaja2 = Kasutaja()
kasutaja3 = Kasutaja()
### täpsustame kasutajate eesnimed
kasutaja1.eesnimi = "Timmu"
kasutaja2.eesnimi = "Jaanus"
kasutaja3.eesnimi = "Tõnu"
### täpsustame kasutajate perenimed
kasutaja1.perenimi = "Kroots"
kasutaja2.perenimi = "Mägi"
kasutaja3.perenimi = "Kunn"
### täpsustame kasutajate asukoha
kasutaja1.asukoht = "Domeen"
kasutaja2.asukoht = "Domeen"
kasutaja3.asukoht = "Workgroup"
### täpsustame kasutajate privileegid
kasutaja1.privileeg = "root"
kasutaja2.privileeg = "kasutaja"
kasutaja3.privileeg = "kasutaja"
### algatame kasutajate kirjeldamise ja tervitamise
kasutaja1.kirjelda_kasutaja()
kasutaja1.tervita_kasutaja()
kasutaja2.kirjelda_kasutaja()
kasutaja2.tervita_kasutaja()
kasutaja3.kirjelda_kasutaja()
kasutaja3.tervita_kasutaja()