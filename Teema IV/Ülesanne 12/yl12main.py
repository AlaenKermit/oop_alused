from yl12jäätisklass import *

# loome 3 eksemplaari ja kasutame neid
restoran1 = JäätiseKiosk("BabyBack Ribs", "Pizza 20€")
restoran2 = JäätiseKiosk("Timmu saiad", "Juustumaitseline Baguette 50€")
restoran3 = JäätiseKiosk("Burgerikuningas", "Jalasalat 5000€ ")

# kutsume eksemplaari meetodid tööle
restoran1.restorani_kirjeldus()
restoran1.ava_restoran()
# teine restoran
restoran2.restorani_kirjeldus()
restoran2.ava_restoran()
# kolmas restoran
restoran3.restorani_kirjeldus()
restoran3.ava_restoran()
# restoran 1 määrame teenindatud külastajate arvu
restoran1.maara_teenindatud_kylalised(123)
# restoran 2 määrame ja lisame teenindatud külastajate arvu
restoran2.maara_teenindatud_kylalised(13)
restoran2.suurenda_teenindatud_kylalised(155)
# Näitame Jäätise Nimekirja!!!
restoran1.näitajäätiseid()