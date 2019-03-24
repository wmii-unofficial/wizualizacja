class Parzysty:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 2
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]


for i in Parzysty("Wizualizacja danych"):
    print(i)