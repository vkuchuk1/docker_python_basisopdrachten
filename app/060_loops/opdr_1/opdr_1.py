# Opdracht 1 loops
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

my_list = []
cijfer = 1
while True:
    cijferinput = input(f"Vul cijfers van 1 tot 10 in ({cijfer}) : ")
    my_list.append(cijferinput)
    cijfer += 1
    if cijfer == 11:
        break
print(*my_list, sep=", ")