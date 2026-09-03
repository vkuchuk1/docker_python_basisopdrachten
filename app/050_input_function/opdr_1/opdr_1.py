# Opdracht 1 input function
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.
a = int(input("Geef de lengte van eerste zijde: "))
b = int(input("Geef de lengte van tweede zijde: "))

c = (a ** 2 + b ** 2) ** 0.5

print("De lengte van de schuine zijde is:", int(c))