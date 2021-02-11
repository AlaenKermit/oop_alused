from random import randint

class Sõdur():
    tervis = 100


def võitlus(inimene1, inimene2):
    while inimene1.tervis > 0 and inimene2.tervis > 0:
        ründaja = randint(1, 2)
        if ründaja == 1:
            inimene1.tervis -= 20
            print("Esimene sõdur lõi")
            if inimene2.tervis == 0:
                print("Esimene sõdur Võitis!!!")
        elif ründaja == 2:
            inimene2.tervis -= 20
            print("Teine sõdur lõi")
            if inimene1.tervis == 0:
                print("Teine sõdur Võitis!!!")