from random import randint

class Sõdur():
    tervis = 100

    def võitlus(self, inimene2):
        while self.tervis > 0 and inimene2.tervis > 0:
            ründaja = randint(1, 2)
            if ründaja == 1:
                print("Esimene sõdur lõi")
                inimene2.tervis -= 20 # eemaldab teiselt sõdurilt 20 elu
                print("Teisel sõduril on alles",inimene2.tervis,"elu") # annab välja palju elusi on alles teisel sõduril peale seda kui esimene sõdur teda lõi
                if inimene2.tervis == 0:
                    print("Esimene sõdur Võitis!!!")
            elif ründaja == 2:
                print("Teine sõdur lõi") # väljastab et teine sõdur lõi
                self.tervis -= 20  # eemaldab esimeselt sõdurilt 20 elu
                print("Esimesel sõduril on alles",self.tervis,"elu") # annab välja palju elusi on alles teisel sõduril peale seda kui esimene sõdur teda lõi
                if self.tervis == 0:
                    print("Teine sõdur Võitis!!!")