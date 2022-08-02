class MonException(Exception):
    def __int__(self):
        Exception(self)

def bar(a, b):
    if (b!= 0):
        return a/b
    else:
        raise MonException("Division par 0")

print("Avant")
try:
    print(bar(1, 0))
except ZeroDivisionError:
    print("Division par 0")
except Exception as e:
    print(e)
except:
    print("Autre erreur")
finally:
    print("Fin")
1/0 #### Exception non gérée
bar(1, 0)
print("Apres")