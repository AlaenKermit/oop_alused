from yl13klass import *

class Admin(Kasutaja):
    privileegid = ["Lisa kasutajad","Eemalda kasutajad","Blokeeri kasutajad","Ära blokeeri kasutajad"]
    def __init__(self, eesnimi, perenimi):
        super().__init__(eesnimi, perenimi)

    def show_privileges(self):
        if Admin.get_privileeg(self) == "root":
            print("Kasutaja " + self.eesnimi + " " + self.perenimi + " on Administraator ja tal on järgnevad privileegid: " + Admin.privileegid[0] + " | " + Admin.privileegid[1] + " | " + Admin.privileegid[2] + " | " + Admin.privileegid[3])
        elif Admin.get_privileeg(self) == "user":
            print("Kasutaja " + self.eesnimi + " " + self.perenimi + " on Kasutaja ja tal on järgnevad privileegid: " + Admin.privileegid[2] + " | " + Admin.privileegid[3])
