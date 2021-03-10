class Kasutaja():
    """Kasutaja kirjeldav klass"""
    def __init__(self, eesnimi, perenimi, kasutajanimi, parool):
        """Kasutaja loomisel kasutatav konstruktor"""
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
        """Kasutaja kirjeldus"""
        print("Inimese nimi on " + str(self.eesnimi) + " " + str(self.perenimi) + " tema asukoht on " + domeen)

class Admin(Kasutaja):
    def __init__(self, eesnimi, perenimi, kasutajanimi, parool):
        super().__init__(eesnimi, perenimi, kasutajanimi, parool)
        self.roll = "root"
        self.privileegid = Privileegid()

class Privileegid():
    def __init__(self):
        self.privileegid = ["Lisa kasutajad","Eemalda kasutajad","Blokeeri kasutajad","Ära blokeeri kasutajad"]

    def show_privileges(self):
        print("Admini privileegid")
        for privileeg in self.privileegid:
            print(privileeg)