
with open("test.txt", "w") as f:
    f.write("Hello world")

with open("test.txt", "r") as f:
    print(f.read())