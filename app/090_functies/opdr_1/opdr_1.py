# Opdracht 1 functies
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7


def write_to_file(my_file, my_tekst):
    with open(my_file, "a") as file:
        file.write(my_tekst + "\n")

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "opdr0901.txt"
write_to_file(my_file, my_tekst)
