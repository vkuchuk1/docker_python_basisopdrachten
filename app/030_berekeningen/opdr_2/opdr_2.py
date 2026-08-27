# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...
try:
    c = float(input("Voer een Celsius hier: "))
    f = float(input("Voer een Fahrenheit hier: "))
    
    celtofar = (c * 9/5) + 32
    fartocel = (f - 32) * 5/9

    print(f"{c} graden Celsius is gelijk aan {celtofar} graden Fahrenheit")
    print(f"{f} graden Fahrenheit is gelijk aan {fartocel} graden Celsius")

except ValueError:
    print("Geen cijfer ingevoerd")