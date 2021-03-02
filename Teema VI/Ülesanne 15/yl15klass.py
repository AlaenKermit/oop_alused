class Inimene:
    def __init__(self, eesnimi, perenimi, kutsekvalifikatsioon, parool = "qwerty"):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.kutsekvalifikatsioon = kutsekvalifikatsioon
        self.sisselogimiskatsed = 0
        self.__parool = parool
        global miinimumlist
        miinimumlist = []

    def maara_parool(self, x):
        self.__parool = x
        print("Parool on määratud!")
        print("ALNKRM v0.1")

    def naita_parool(self):
        print(self.eesnimi + " parool on praegu " + self.__parool)

    def kasutajanimi(self):
        print(self.eesnimi.lower() + "." + self.perenimi.lower())
    def parool(self):
        self.naita_parool()

    def kontrolli_parool(self, x):
        if len(x) >= 6 and len(x) <= 10:
            self.maara_parool(x)
            print("Parooli muutmine õnnestunud!")
        elif len(x) < 6:
            print("Parooli muutmine ebaõnnestunud")
            print("Parool liiga lühike, peab olema vähemalt 6 tähte")
        elif len(x) > 10:
            print("Parooli muutmine ebaõnnestunud")
            print("Parool liiga pikk, peab olema vähem kui 10 tähte")

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
        print("Tere! Olen " + self.eesnimi + " " + self.perenimi + ". Mu kasutajanimi on " + self.eesnimi.lower() + "." + self.perenimi.lower() + " ja parool on " + self.__parool)