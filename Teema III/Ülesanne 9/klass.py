class Restoran():
    def __init__(self, restorani_nimi, soogi_tyyp):
        self.restorani_nimi = restorani_nimi
        self.soogi_tyyp = soogi_tyyp
        self.teenindatud_kylastajad = 0

    def restorani_kirjeldus(self):
        print("Restoran " + str(self.restorani_nimi) + " söögi tüüp " + str(self.soogi_tyyp))

    def ava_restoran(self):
        print("Restoran " + str(self.restorani_nimi) + " on avatud!")

    def määra_teenindatud_kylalised(self, x):
        self.teenindatud_kylastajad = x
        print("Määratud et hetkel on teenindatud", x, "külalist restoranis " + str(self.restorani_nimi))

    def suurenda_teenindatud_kylalised(self, x):
        self.teenindatud_kylastajad += x
        print("Restoranis " + str(self.restorani_nimi) + " on hetkel teenindatud külastajate arvu suurendatud", x,
              "võrra")
        print("Kokku on teenindatud " + str(self.teenindatud_kylastajad) + " külastajat restoranis " + str(
            self.restorani_nimi))
