class Kasutaja():
    """Kasutaja kirjeldav klass"""
    def __init__(self, eesnimi, perenimi, kasutajanimi, parool):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.kasutajanimi = kasutajanimi
        self.parool = parool
        self.roll = "user"

    def set_domain(self, x):
        self._domain = x
    def set_privileeg(self, x):
        self._privileeg = x
    def get_domain(self):
        return self._domain
    def get_privileeg(self):
        return self._privileeg
    def kirjelda_kasutajat(self, domeen):
        print("Inimese nimi on " + str(self.eesnimi) + " " + str(self.perenimi) + " tema asukoht on " + domeen)