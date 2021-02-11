from random import randint
class Sõdur():
    tervis = 100
    kord = 0

    def võitlus(inimene):
        if inimene.tervis >= 1:
            inimene.kord = randint(0,1)
            if inimene.kord == 1:
                inimene.tervis = inimene.tervis - 20
                print(inimene.tervis)