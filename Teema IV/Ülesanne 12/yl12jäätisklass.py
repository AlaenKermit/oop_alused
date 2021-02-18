from yl12klass import *


class JäätiseKiosk(Restoran):
    kounter = 0
    jäätisevalik = ["1. Vanilje","2. Maasikas","3. Õun","4. Pirn","5. BurgeriKuningaJalaSalat"]
    def __init__(self, x, y):
        super().__init__(x, y)

    def näitajäätiseid(self):
        print("\n".join(self.jäätisevalik))
