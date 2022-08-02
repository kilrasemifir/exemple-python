"""
Ce module definit une classe pour representer une distance en metres, yards et miles
"""


class Distance:

    def __init__(self, **kwargs):
        if 'metres' in kwargs:
            self.metres = kwargs['metres']
        elif 'yards' in kwargs:
            self.metres = kwargs['yards'] * 0.9144
        elif 'miles' in kwargs:
            self.metres = kwargs['miles'] * 1609.34
        else:
            self.metres = 0

    @property
    def metres(self):
        return self._metres

    @metres.setter
    def metres(self, m):
        self._metres = m

    @property
    def yards(self):
        return self._metres / 0.9144

    @yards.setter
    def yards(self, y):
        self._metres = y * 0.9144

    @property
    def miles(self):
        return self._metres / 1609.34

    @miles.setter
    def miles(self, mi):
        self._metres = mi * 1609.34

    def __add__(self, other):
        """Additionne deux distances"""
        return Distance(metres=self.metres + other.metres)

    def __sub__(self, other):
        """"Soustrait deux distances"""
        return Distance(metres=self.metres - other.metres)

    def __mul__(self, other):
        """Multiplie une distance et un scalaire"""
        if type(other) in [int, float]:
            return Distance(metres=self.metres * other)
        else:
            raise TypeError("Multiplication impossible entre une distance et une valeur non scalaire")

    def __truediv__(self, other):
        """Divise une distance et un scalaire"""
        if type(other) in [int, float]:
            return Distance(metres=self.metres / other)
        else:
            raise TypeError("Division impossible entre une distance et une valeur non scalaire")

d = Distance(metres=10)
d2 = Distance(yards=10)

d3 = d + d2
d4 = d3 - d2
d5 = d * 2
try:
    d6 = d * d2
except TypeError:
    print("Multiplication impossible entre une distance et une valeur non scalaire")

print(d3.metres, d4.metres)
