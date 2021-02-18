class Ristkülik:
    def __init__(self, laius, korgus, symbol):
        self.width = int(laius)
        self.height = int(korgus)
        self.symbol = str(symbol)
    def __str__(self):
        ruut = []  # nimekiri symbolite kordamiseks
        for i in range(self.height):  # ridade arv
            ruut.append(self.symbol * self.width)  # symbol tuleb korrutada laiuse arvuga
        ruut = '\n'.join(ruut)  # teisendame nimekirja stringiks
        return ruut
    def __add__(self, x):
        self.width = self.width + x.width
        self.height = self.height + x.height
        self.symbol = self.symbol

kujund1 = Ristkülik(10, 3, '*')
print(kujund1)
kujund2 = Ristkülik(8, 3, 'z')
print(kujund2)

kujund1.__add__(kujund2)
print(kujund1)

#im a maniac
#maaaaaniac
#on the floor