from yl11klass import *

armee1 = []
armee2 = []


class Sodur(Inimene):
    def __init__(self):
        super().__init__()

    def armeejagaja(self):
        for kord in range(1, 21, 1):
            armee = randint(1, 2)
        if armee == 1:
            print("Sõdur " + str(self.idnumber) + " on armees nr 1")
            armee1.append(self)
        elif armee == 2:
            print("Sõdur " + str(self.idnumber) + " on armees nr 2")
            armee2.append(self)