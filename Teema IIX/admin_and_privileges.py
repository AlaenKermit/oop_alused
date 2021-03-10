from user import *
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