class Point:
    counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.counter += 1
        print("init: counter = {}".format(self.counter))


p1 = Point(2, 3)
p2 = Point(4, 3)
p3 = Point(5, 3)

print(Point.counter)
print(p1.counter)
print(p2.counter)
print(p3.counter)
