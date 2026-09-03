# Opdracht 2 berekeningen
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7

# Hier komt je code...

gasten = ["Vlady", "Paul", "Kees", "Marie", "Hilda"]
for names in gasten:
    print(names)
input("Druk op enter om verder te gaan...")

gasten.remove("Marie")
for names in gasten:
    print(names)
input("Druk op enter om verder te gaan...")

gasten.insert(3, "George")
for names in gasten:
    print(names)
input("Druk op enter om verder te gaan...")

exit