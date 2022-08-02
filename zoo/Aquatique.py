class Aquatique:
    def __init__(self, vitesse):
        self.vitesse_aquatique = vitesse

    def nager(self):
        #Nouvelle syntaxe: print(f"Je nage à la vitesse de {self.vitesse_aquatique}")
        print("Je nage à la vitesse de {}".format(self.vitesse_aquatique))

class Terrestre:
    def __init__(self): pass

    def marcher(self):
        print("Je marche")

class Aerien:
    def __init__(self): pass

    def voler(self):
        print("Je vol")