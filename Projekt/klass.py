# Allan Kerme
# Kristjan Kuus

class elektroonika():
    def __init__(self, nimi, töötab=0):
        self.elektroonianimi = nimi
        self.töötab = töötab

    def check_state(self):
        if self.töötab == 0:
            print("Seade on hektel väljas")
            return "väljas"
        else:
            print("Seade on hetkel sees")
            return "sees"

    def kirjeldus(self):
        print("Selleks seadmeks on " + str(self.elektroonianimi + " ja see seade on hetkel " + str(elektroonika.check_state(self))))  # abc = elektroonika("Pliit")

    def lüliti(self):
        elektroonika.check_state(self)
        sisend = str(input("Kas soovite olekut vahetada [J(jah)/E(ei)?"))
        if sisend == "J":
            if self.töötab == 0:
                self.töötab = 1
            elif self.töötab == 0:
                self.töötab = 1
        else:
            print("Te kas ei soovinud seade olekut muuta või sisestaasite vale sisendi!")