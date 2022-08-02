from heapq import heappop, heappush

mon_tas = []

heappush(mon_tas, "Hello") # Ajoute "Hello" au tas
print("1",mon_tas)
heappush(mon_tas, "World")
print("2",mon_tas)
heappush(mon_tas, "!")
print("3", mon_tas)

for i in range(3):
    print(mon_tas, heappop(mon_tas))