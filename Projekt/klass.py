# Allan Kerme
# Kristjan Kuus

class elektroonika(): # Klass
    def __init__(self, nimi, töötab=0): 
        self.elektroonianimi = nimi
        self.töötab = töötab

    def check_state(self): # funktsioon mis kontrollib kas objekt töötab või mitte ja tagastab vastuse
        if self.töötab == 0:
            print("Seade on hektel väljas")
            return "väljas"
        else:
            print("Seade on hetkel sees")
            return "sees"

    def kirjeldus(self): # kirjeldus
        print("Selleks seadmeks on " + str(self.elektroonianimi + " ja see seade on hetkel " + str(elektroonika.check_state(self))))  # abc = elektroonika("Pliit")

    def lüliti(self): # lülitab ümber
        elektroonika.check_state(self)
        sisend = str(input("Kas soovite olekut vahetada [J(jah)/E(ei)?"))
        if sisend == "J":
            if self.töötab == 0:
                self.töötab = 1
            elif self.töötab == 1:
                self.töötab = 0
        else:
            print("Te kas ei soovinud seade olekut muuta või sisestaasite vale sisendi!")
