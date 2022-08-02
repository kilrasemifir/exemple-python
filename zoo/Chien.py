from animal import Animal
from Aquatique import Terrestre, Aquatique
from time import sleep
class Chien(Animal, Terrestre, Aquatique):
    def __init__(self, taille, nom):
        Animal.__init__(self, taille)
        Aquatique.__init__(self, 10)
        self._nom = nom.capitalize()
        # self.nom = nom.capitalize()

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, n):
        self._nom = n.capitalize()

medor = Chien(taille=120, nom="medor")
medor.nom = "droupi"

print(medor.taille, medor.nom == "Droupi")
medor.se_nourrir()
medor.nager()
medor.marcher()
# sleep(0.1)
# medor.voler() ## ERREUR!!!
