"""
Ce module par les getters et setters en python
"""
class Temperature:
    """Classe représentant une température en Kelvin et permet de convertir en autre température"""

    def __init__(self, kelvin=False, celsius=False, fahrenheit=False):
        """
        On utilise en interne _kelvin pour ne pas avoir de problème avec les getters et setters
        """
        if kelvin:
            self._kelvin = kelvin
        elif celsius:
            self._kelvin = celsius + 273.15
        elif fahrenheit:
            self._kelvin = (fahrenheit - 32) * 5/9 + 273.15
        else:
            self._kelvin = 0

    @property
    def kelvin(self):
        """getter de la température en Kelvin"""
        return self._kelvin

    @property
    def celsius(self):
        """getter de la température en Celsius"""
        return self._kelvin - 273.15

    @property
    def fahrenheit(self):
        """getter de la température en Fahrenheit"""
        return self._kelvin * 9/5 - 459.67

    @kelvin.setter
    def kelvin(self, K):
        """setter de la température en Kelvin"""
        self._kelvin = K

    @celsius.setter    
    def celsius(self, C):
        """setter de la température en Celsius"""
        self._kelvin = C + 273.15

    @fahrenheit.setter
    def fahrenheit(self, F):
        """setter de la température en Fahrenheit"""
        self._kelvin = (F + 459.67) * 5/9

# Création d'une instance de la classe Temperature
temp = Temperature(kelvin=300)
print(temp.celsius, "C")
print(temp.fahrenheit, "F")
print(temp.kelvin, "K")
print("Nouvelle temperature:")
temp.celsius = 22
print(temp.celsius, "C")
print(temp.fahrenheit, "F")
print(temp.kelvin, "K")
