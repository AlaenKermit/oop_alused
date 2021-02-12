class Kasutaja():
    def __init__(self, eesnimi, perenimi):
        self.eesnimi = eesnimi
        self.perenimi = perenimi

    def set_domain(self, x):
        self._domain = x
    def set_privileeg(self, x):
        self._privileeg = x
    def get_domain(self):
        return self._domain
    def get_privileeg(self):
        return self._privileeg

    def kirjelda_kasutajat(self, domeen, privileeg):
        print("Inimese nimi on " + str(self.eesnimi) + " " + str(self.perenimi) + " tema asukoht on " + domeen + " ja privileeg on " + privileeg)