# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...
try:
    c = int(input("Voer een Celsius hier: "))
    f = int(input("Voer een Fahrenheit hier: "))
    
    print("c =", c)
    print("f =", f)
except ValueError: 
    print("Verkeerde invoer")
celtofar = (c * 9/5) + 32
fartocel = (f - 32) * 5/9
print(f"{c} graden Celsius is gelijk aan {celtofar} graden Fahrenheit")
print(f"{f} graden Fahrenheit is gelijk aan {fartocel} graden Celsius")