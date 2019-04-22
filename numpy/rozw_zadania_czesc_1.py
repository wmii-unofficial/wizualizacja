import numpy as np

# zadanie 1
def zad1():
    return np.arange(2,20*2+1,2)

# zadanie 2
def zad2():
    tab_float = np.arange(1,10, 0.2)
    tab_int = tab_float.astype('int64')
    print(tab_float)
    print(tab_int)

# zadanie 3
def zad3(n):
    return np.arange(1,n*n+1).reshape((n,n))

# zadanie 4
def zad4(n, base):
    return np.logspace(1, n, num=n, base=base)

# zadanie 5
def zad5(n):
    return np.diag(range(n, 0, -1))

# zadanie 6
def zad6():
    # wyrazy jako wektory znaków (liter)
    malina = np.array(list('malina'))
    lizak = np.array(list('lizak'))
    jagoda = np.array(list('jagoda'))

    # przygotowanie "pustej" tablicy 6x6 wypełnionej pustym stringiem
    wykreslanka = np.zeros((6, 6), dtype=str)
    # lub
    wykreslanka = np.empty((6, 6), dtype='str')
    # lub tak
    # wykreslanka = np.full((6,6),"",dtype='str')
    # można też bardziej "na piechotę"

    # teraz np. za pomocą wycinków (slice) możemy nie tylko zwracać
    # określone fragmenty macierzy, ale wstawiać tam wartości
    # należy pamiętać, że rozmiar wycinka musi być taki sam jak
    # rozmiar danych, które chcemy tam umieścić
    wykreslanka[:, 0] = malina
    wykreslanka[2,:5] = lizak
    wykreslanka[5,::-1] = jagoda
    # za pomocą np.put możemy również wstawiać dane do macierzy określając zbiór indeksów
    # na których odpowiadające wartości stawianego wektora mają się znaleźć
    # ale tutaj numeracja indeksów jest "globalna" gdzie indeks 0 to wiersz 0 i kolumna 0
    # a kolejne numery są naliczane do prawej strony np.
    # 0  1  2  3
    # 4  5  6  7
    # 8  9 10 11 itd.
    # np.put(wykreslanka, [ 0, 6, 12, 18, 24, 30 ], wyraz1)
    # np.put(wykreslanka, range(12, 17), wyraz2)
    print(wykreslanka)

# zadanie 7
def zad7(n):
    mat = np.diag([2 for _ in range(n)])
    for indeks in range(1, n):
        vec = [2+(2*indeks) for _ in range(n-indeks)]
        mat += np.diag(vec, indeks)
        mat += np.diag(vec, -indeks)
    print(mat)

# zadanie 8
def zad8(tab, kierunek='poziomo'):
    if kierunek == 'poziomo':
        # nieparzysta liczba wierszy
        if tab.shape[0] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę wierszy")
            return
        p1 = tab[0:int(tab.shape[0]/2), :]
        p2 = tab[int(tab.shape[0]/2):, :]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)
    elif kierunek == "pionowo":
        if tab.shape[1] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę wierszy")
            return
        p1 = tab[:, 0:int(tab.shape[1]/2)]
        p2 = tab[:, int(tab.shape[0] / 2):]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)

# zadanie 9
def zad9(n):
    # funkcja wewnętrzna
    def fibo(n):
        if n == 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [1, 1]
        else:
            fibos = [1, 1]
            for indeks in range(n-2):
                fibos.append(fibos[-1] + fibos[-2])
            return fibos
    # print(fibo(n))
    # teraz Numpy array
    import math as m
    shape = int(m.sqrt(n))
    return np.array(fibo(n)).reshape((shape, shape))

print(zad1())
zad2()
print(zad3(5))
print(zad4(4, 2))
print(zad5(4))
zad6()
zad7(5)
zad8(np.arange(36).reshape((6,6)))
zad8(np.arange(36).reshape((6,6)), kierunek='pionowo')
print(zad9(25))
