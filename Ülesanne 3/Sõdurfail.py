from random import randint

class Sõdur():
    tervis = 100


def võitlus(inimene1, inimene2):
    while inimene1.tervis > 0 and inimene2.tervis > 0:
        ründaja = randint(1, 2)
        if ründaja == 1:
            print("Esimene sõdur lõi")
            inimene2.tervis -= 20 # eemaldab teiselt sõdurilt 20 elu
            print("Teisel sõduril on alles",inimene2.tervis,"elu")
            if inimene2.tervis == 0:
                print("Esimene sõdur Võitis!!!")
        elif ründaja == 2:
            print("Teine sõdur lõi")
            inimene1.tervis -= 20  # eemaldab esimeselt sõdurilt 20 elu
            print("Esimesel sõduril on alles",inimene1.tervis,"elu")
            if inimene1.tervis == 0:
                print("Teine sõdur Võitis!!!")