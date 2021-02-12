class Kasutaja():
    eesnimi = ""
    perenimi = ""
    asukoht = ""
    privileeg = ""

    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on " + str(self.eesnimi) + " ja perekonnanimi on " + str(self.perenimi) + " ja kasutaja asub " + str(self.asukoht) + " ja kasutaja privileegid on " + str(self.privileeg))

    def tervita_kasutaja(self):
        print("Tere tulemast " + str(self.eesnimi), str(self.perenimi))