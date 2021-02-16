from random import randint


class Inimene():
    def __init__(self):
        self.identifikatsioon = 0
        global identifikatsioon
        identifikatsioon = 0

    def assign_id(self):
        identifikatsioon += 1

    def info(self):
        print("Sõduri ID on ", str(self.identifikatsioon))


class Sodur(Inimene):
    def __init__(self, armee):
        super().__init__(armee)
        self.armee = armee
        self.armee = randint(1, 2)
