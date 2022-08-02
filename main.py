
import lib
from lib import PI
print(lib.PI)
print(PI)

nom = "Raoux"


message = f"Bonjour {nom}"

age = 12

if age < 18:
    print(message)

while age < 20:
    print(age)
    age += 1

for i in range(10):
    print(i)
    
li = [1, 2, 3, 4, 5]

for item in li:
    print(item)
    
if __name__ == "__main__":
    print("hello")