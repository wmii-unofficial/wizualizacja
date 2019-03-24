class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print("[MATERIAL] Rodzaj: {}, dlugosc: {}, szerokosc: {}".format(self.rodzaj, self.dlugosc, self.szerokosc))


class Ubrania(Material):
    def __init__(self, rozmiar, dla_kogo, kolor, rodzaj, dlugosc, szerokosc):
        super().__init__(rodzaj, dlugosc, szerokosc)
        self.rozmiar = rozmiar
        self.dla_kogo = dla_kogo
        self.kolor = kolor

    def wyswietl_nazwe(self):
        super().wyswietl_nazwe()
        print("[UBRANIA] rozmiar: {}, dla kogo: {}, kolor: {}".format(self.rozmiar, self.dla_kogo, self.dlugosc))


class Sweter(Ubrania):
    def __init__(self, rozmiar, dla_kogo, kolor, rodzaj, dlugosc, szerokosc, rodzaj_swetra):
        super().__init__(rozmiar, dla_kogo, kolor, rodzaj, dlugosc, szerokosc)
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_nazwe(self):
        super().wyswietl_nazwe()
        print("[SWETER] Rodzaj: {}".format( self.rodzaj_swetra))


m1 = Material(rodzaj="milutki", dlugosc="dazy do nieskonczonosci", szerokosc="dazy do zera")
m1.wyswietl_nazwe()
print()

u1 = Ubrania("XS", "Antman", "moro", "tajemniczy", "dla mrowki", "dla mrowki")
u1.wyswietl_nazwe()
print()

s1 = Sweter("duzy", "informatyka", "szary", "fajny", "1234", "5678", "+5 do C++")
s1.wyswietl_nazwe()
print()