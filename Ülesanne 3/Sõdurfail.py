from random import randint

class Soodur():
    tervis = 100

    def voitlus(self, vaenlane):
        while vaenlane.tervis > 0 and self.tervis > 0:
            rundaja = randint(1, 2)
            if rundaja == 1:
                print("Esimene sõdur lõi")
                vaenlane.tervis -= 20 # eemaldab teiselt sõdurilt 20 elu
                print("Teisel sõduril on alles", vaenlane.tervis, "elu") # annab välja palju elusi on alles teisel
                # sõduril peale seda kui esimene sõdur teda lõi
                if vaenlane.tervis == 0:
                    print("Esimene sõdur Võitis!!!")
            elif rundaja == 2:
                print("Teine sõdur lõi") # väljastab et teine sõdur lõi
                self.tervis -= 20  # eemaldab esimeselt sõdurilt 20 elu
                print("Esimesel sõduril on alles", self.tervis, "elu") # annab välja palju elusi on alles teisel sõduril peale seda kui esimene sõdur teda lõi
                if self.tervis == 0:
                    print("Teine sõdur Võitis!!!")