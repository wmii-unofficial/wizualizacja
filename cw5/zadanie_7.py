class Samogloski:
    def __init__(self, data):
        self.data = data
        self.index = -1
        if not isinstance(data, str):
            raise TypeError("lol, nie")

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 1
        while self.index < len(self.data) and not self.data.lower()[self.index] in ['a', 'e', 'y', 'i', 'o', 'u']:
            self.index = self.index + 1
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]


for i in Samogloski("Wizualizacja dAnych"):
    print(i)

for i in Samogloski("WizUalizacja dAnych"):
    print(i)