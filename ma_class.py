class MaClass():
    """Class pour une demo
    """    
    def __init__(self, nom, taille):
        self._nom = nom
        self._taille = taille
        
    def get_nom(self):
        return self._nom
    
    def get_taille(self):
        return self._taille
    
    def set_nom(self, nom):
        self._nom = nom.lower()
    
    def set_taille(self, taille):
        self._taille = taille

    def vers_chaine(self):
        """Trasnforme l'instance en un str
        """
        return f"nom: {self._nom}; taille: {self._taille}"
    
    def parametres(self, param1, param2):
        """Fonctiona vec des params
        """
        return param1 + param2
    
    @staticmethod
    def build(nom, taille):
        if taille < 100:
            print("Attention, la taille doit etre sup a 1m")
        return MaClass(nom.lower(), taille)
    
    @staticmethod
    def build_many(nb):
        results = []
        for i in range(nb):
            results.append(MaClass(nb, 150+nb*10))
        return results

    @staticmethod
    def addition(*args):
        """Definition"""
        print(args)
        return sum(args)

    @staticmethod
    def foo(*args, **kwargs):
        """Definition"""
        print("args  =", args)
        print("kwargs=", kwargs)

# foo(1, 3, 4)
# foo(1, nom="Toto")
# print(addition())


instance = MaClass("Raoux", 180)
# instance.addition(1, 2)
# instance.foo(1, 2, toto=True)
instance.nom = "Toto"
print(instance._nom, instance.nom)

MaClass.addition(1, 2, 3)
MaClass.foo()
