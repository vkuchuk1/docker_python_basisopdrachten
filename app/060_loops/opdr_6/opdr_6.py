# Opdracht 3 input functie
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7

# Hier komt je code...

# Hier start de for-loop

pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']
print(pizzas)

input("Klik op Enter om te sorteren...")
print(sorted(pizzas))
pizzas = sorted(pizzas)

npizza = input("Voeg jouw pizza toe: ")
pizzas.append(npizza)
print(pizzas)

input("Klik op Enter om het slechtste pizza te verwijderen...")
pizzas.remove(pizzas[2])
print(pizzas)

input("Klik op Enter om eerste drie pizza's te printen... ")
print(pizzas[:3])

input("Klik op Enter om middelste pizza te printen... ")
print(pizzas[2:3])

input("Klik op Enter om de laatste drie pizza's te printen... ")
print(pizzas[-3:])