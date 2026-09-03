# Opdracht 2 condities
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7

# Hier komt je code...

# Hier start de for-loop

my_list = [43948, 878768, 38768, 87555, 765765]

for getal in my_list:
    if getal % 3 == 0:
        print(getal)
    else:
        print(f"{getal} is niet deelbaar door 3")