class Andmed():
    """
    Allan Kerme oli siin!
    """

    def __init__(self, *info):  # <------ |
        self.info = list(info)  # ------> |

    def __getitem__(self, index):  # väga kasulik!!!
        return self.info[index]


class Opilane():
    def __init__(self, nimi):
        self.nimi = nimi
        self.smarts = []

    def opib(self, teema):
        self.smarts.append(teema)

    def kirjeldus(self):
        print("Õpilase " + self.nimi + " teadmised on järgnevad:")
        for teema in self.smarts:
            print("* " + teema)
        print("LÕPP")

    def unutab(self, teema):
        self.smarts.remove(teema)

class Opetaja():
    def __init__(self, nimi):
        self.nimi = nimi
    def opetab(self, teema, *opilased):
        for i in opilased:
            i.opib(teema)
