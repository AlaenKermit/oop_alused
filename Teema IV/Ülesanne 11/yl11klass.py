from random import randint
class Inimene():
    järjekorranumber = 0

    def __init__(self):
        self.idnumber = self.järjekorranumber + 1
        Inimene.järjekorranumber += 1

    def info(self):
        print("Sõduri ID on " + str(self.idnumber))