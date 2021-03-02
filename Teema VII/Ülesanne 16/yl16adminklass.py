from yl16klass import *

class Privileegid(Kasutaja):
    def __init__(self, eesnimi, perenimi, privileegid = ["Lisa kasutajad","Eemalda kasutajad","Blokeeri kasutajad","Ära blokeeri kasutajad"]):
        super().__init__(eesnimi, perenimi)
        self.privileegid = privileegid

    def show_privileges(self):
        if Admin.get_privileeg(self) == "root":
            print("Kasutaja " + self.eesnimi + " " + self.perenimi + " on Administraator ja tal on järgnevad privileegid: " + Privileegid.privileegid[0] + " | " + Privileegid.privileegid[1] + " | " + Privileegid.privileegid[2] + " | " + Privileegid.privileegid[3])
        elif Admin.get_privileeg(self) == "user":
            print("Kasutaja " + self.eesnimi + " " + self.perenimi + " on Kasutaja ja tal on järgnevad privileegid: " + Privileegid.privileegid[2] + " | " + Privileegid.privileegid[3])

class Admin(Privileegid):
    privileegid = Privileegid("midagi on valesti", "midagi on väga väga väga valesti")
    def __init__(self, eesnimi, perenimi):
        super().__init__(eesnimi, perenimi)