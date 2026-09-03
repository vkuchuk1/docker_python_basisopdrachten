# Opdracht 3 input functie
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7

# Hier komt je code...

steden = input("Geef de namen van een steden: ").split(", ")

steden.sort(reverse=True)

print(", ".join(steden))