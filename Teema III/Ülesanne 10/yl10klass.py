class Inimene:
    def __init__(self, eesnimi, perenimi, kutsekvalifikatsioon):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.kutsekvalifikatsioon = kutsekvalifikatsioon
        self.sisselogimiskatsed = 0
        global miinimumlist
        miinimumlist = []

    def getmin(self):
        miinimum = self.kutsekvalifikatsioon
        miinimumlist.append(miinimum)

    def suurenda_sisselogimiskatsed(self):
        self.sisselogimiskatsed += 1
        print("Kasutaja " + str(self.eesnimi), str(self.perenimi) + " on hetkel loginud kokku " + str(self.sisselogimiskatsed) + " korda")

    def reset_sisselogimiskatsed(self):
        self.sisselogimiskatsed = 0
        print("resetitud sisselogimiskatsed kasutajal " + str(self.eesnimi), str(self.perenimi) + " ja nüüd on " + str(self.sisselogimiskatsed) + " korda sisse logitud")

    def __del__(self):
        if self.kutsekvalifikatsioon == min(miinimumlist):
            print(str(self.eesnimi) + " " + str(self.perenimi) + " ADIOS AMIGO! Ei ole piisavalt pädev kutsekvalifikatsioon!")
        else:
            print("Liigume edasi")

    def tutvustus(self):
        print("Tere! Olen " + self.eesnimi + " " + self.perenimi)
