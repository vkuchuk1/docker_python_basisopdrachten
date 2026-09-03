# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

input_leeftijd = int(input("Voer uw leeftijd in: "))
if input_leeftijd < 0 or input_leeftijd > 150:
    print("Ongeldige leeftijd")
elif input_leeftijd >= 0 and input_leeftijd <= 2:
    korting = kortings_percentages["baby"]
    print("U behoort bij groep baby's")
    print(f"U krijgt {korting}% korting.")
    print(f"U betaalt daarom {normale_toegangsprijs * (1 - korting / 100)} euro.")
elif input_leeftijd >= 3 and input_leeftijd <= 18:
    korting = kortings_percentages["kinderen"]
    print("U behoort bij groep kinderen")
    print(f"U krijgt {korting}% korting.")
    print(f"U betaalt daarom {normale_toegangsprijs * (1 - korting / 100)} euro.")
elif input_leeftijd >= 19 and input_leeftijd <= 64:
    korting = kortings_percentages["volwassenen"]
    print("U behoort bij groep volwassenen")
    print(f"U krijgt {korting}% korting.")
    print(f"U betaalt daarom {normale_toegangsprijs * (1 - korting / 100)} euro.")
elif input_leeftijd >= 65 and input_leeftijd <= 150:
    korting = kortings_percentages["ouderen"]
    print("U behoort bij groep ouderen")
    print(f"U krijgt {korting}% korting.")
    print(f"U betaalt daarom {normale_toegangsprijs * (1 - korting / 100)} euro.")
