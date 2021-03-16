from oppimine import *

aineteemad = Andmed("OOP põhimõtted", "Klassid ja Objektid", "Konstruktor")
print("Aine teemad: ")
for teema in aineteemad:
    print("* " + teema)

Timmu = Opilane("Timmu")
Lisette = Opilane("Lisette")
Anna = Opetaja("Anna")

Timmu.kirjeldus()
Timmu.opib(aineteemad[0])
Timmu.kirjeldus()

Anna.opetab(aineteemad[1], Timmu, Lisette)
Lisette.kirjeldus()
Timmu.kirjeldus()

print("UNUSTAMISE TEST")
print("Timmu unustab ära " + aineteemad[1])
Timmu.unutab(aineteemad[1])
Timmu.kirjeldus()