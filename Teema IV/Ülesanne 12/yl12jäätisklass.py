from yl12klass import *


class JäätiseKiosk(Restoran):
    jäätisevalik = ["Vanilje","Maasikas","Õun","Pirn","BurgeriKuningaJalaSalat"]
    def __init__(self, x, y):
        super().__init__(x, y)

    def näitajäätiseid(self):
        print("\n".join(self.jäätisevalik))
