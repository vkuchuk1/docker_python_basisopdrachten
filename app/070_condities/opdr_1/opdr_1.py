# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

import numbers


my_list = []
cijfer = 1
while True:
    getal = int(input("Voer een getal in: "))
    my_list += [getal]
    cijfer += 1
    if cijfer == 11 and 4 in my_list:
        start_index = my_list.index(4)
        print(my_list[start_index:])