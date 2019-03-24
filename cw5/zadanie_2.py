class Kwadrat():
    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return "Kwadrat o boku {}".format(self.x)

    def __add__(self, other):
        return Kwadrat(self.x+other.x)

    def __ge__(self, other):
        return self.x > other.x


k1 = Kwadrat(2)
k2 = Kwadrat(3)
print(k1)
print(k1+k2)
print(k1 <= k2)
