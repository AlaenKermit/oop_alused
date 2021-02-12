class Inimene:
    def __init__(self, eesnimi, perenimi, kutsekvalifikatsioon):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.kutsekvalifikatsioon = kutsekvalifikatsioon
        global miinimumlist
        miinimumlist = []

    def getmin(self):
        miinimum = self.kutsekvalifikatsioon
        miinimumlist.append(miinimum)

    def __del__(self):
        if self.kutsekvalifikatsioon == min(miinimumlist):
            print(str(self.eesnimi) + " " + str(self.perenimi) + " ADIOS AMIGO!")
        else:
            print("Jeeee")

    def tutvustus(self):
        print("Tere! Olen " + self.eesnimi + " " + self.perenimi)
