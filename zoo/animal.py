class Animal:
    def __init__(self, taille):
        self._taille = taille

    @property
    def taille(self):
        return self._taille

    @taille.setter
    def taille(self, t):
        self._taille = t

    def se_nourrir(self):
        print("Je me nourris")

