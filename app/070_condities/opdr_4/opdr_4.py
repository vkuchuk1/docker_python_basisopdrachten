# Opdracht 4 condities
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = toppings

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

if keuze == "olijven":
    print(f"U heeft {keuze} gekozen. De prijs is {toppings[0][1]} euro.")
elif keuze == "kaas":
    print(f"U heeft {keuze} gekozen. De prijs is {toppings[1][1]} euro.")
elif keuze == "salami":
    print(f"U heeft {keuze} gekozen. De prijs is {toppings[2][1]} euro.")  
elif keuze == "pepperoni":
    print(f"U heeft {keuze} gekozen. De prijs is {toppings[3][1]} euro.") 
elif keuze == "ansjovis":
    print(f"U heeft {keuze} gekozen. De prijs is {toppings[4][1]} euro.")
else:
    print("Deze topping is niet beschikbaar.")