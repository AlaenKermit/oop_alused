class Restoran():
    restorani_nimi = ""
    soogi_tyyp = ""

    def restorani_kirjeldus(self):
        print("Restoran " + str(self.restorani_nimi) + " söögi tüüp " + str(self.soogi_tyyp))

    def ava_restoran(self):
        print("Restoran on avatud!")
