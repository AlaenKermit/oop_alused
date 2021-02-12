from klass import *
# loome 3 eksemplaar
restoran1 = Restoran()
restoran2 = Restoran()
restoran3 = Restoran()
# määrame eksemplaari atribuutidele konkreetsed väärtused
restoran1.restorani_nimi = "Hesburger"
restoran1.soogi_tyyp = "Burgerid"
### teine restoran
restoran2.restorani_nimi = "Timmu saiad"
restoran2.soogi_tyyp = "Saiad"
### kolmas restoran
restoran3.restorani_nimi = "Jaanuse köök"
restoran3.soogi_tyyp = "Kartulipuder hakklihakastmega"
# kutsume eksemplaari meetodid tööle
restoran1.restorani_kirjeldus()
restoran1.ava_restoran()
### teine restoran
restoran2.restorani_kirjeldus()
restoran2.ava_restoran()
### kolmas restoran
restoran3.restorani_kirjeldus()
restoran3.ava_restoran()

