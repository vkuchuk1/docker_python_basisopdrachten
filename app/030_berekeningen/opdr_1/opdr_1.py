# Opdracht 1 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

vriends = ["joe", "bob", "fred"]
leeftijd_joe = 23
leeftijd_bob = 15
leeftijd_fred = 22
for vriend in vriends:
    vriend1 = "joe"
    vriend2 = "bob"
    vriend3 = "fred"
    if vriend == "joe":
        print(vriend, "=", leeftijd_joe)
    elif vriend == "bob":
        print(vriend, "=", leeftijd_bob)
    elif vriend == "fred":
        print(vriend, "=", leeftijd_fred)
print(f"Dit weten we over", vriend1 , vriend2, "en",  vriend3)
total = leeftijd_joe + leeftijd_bob + leeftijd_fred
print(f"De totale waarde van alle leeftijden bij elkaar opgeteld = ", total)
print(f"De gemiddelde leeftijd van deze boys is: {int(total / 3)}")