class Fractie(object):
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator} / {self.numitor}"

    def __add__(self, other):
        if self.numitor == other.numitor:
            return Fractie(self.numarator + other.numarator, self.numitor)
        return Fractie(self.numarator * other.numitor + self.numitor * other.numarator, self.numitor * other.numitor)

    def __sub__(self, other):
        if self.numitor == other.numitor:
            return Fractie(self.numarator - other.numarator, self.numitor)
        return Fractie(self.numarator * other.numitor - self.numitor * other.numarator, self.numitor * other.numitor)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)


rez1 = Fractie(10, 2) + Fractie(11, 2)
rez2 = Fractie(10, 6) + Fractie(10, 3)
print(rez1)
print(rez2)
print(rez1.inverse())
