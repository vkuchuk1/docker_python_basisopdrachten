# Opdracht 1 functies
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7


def kubus_vol(m):
    kubus = m * m * m
    return kubus

def bol_vol(r):
    bol = (4/3) * 3.14159 * (r ** 3)
    return bol

zijde = 5
radius = 4

print(f"De inhoud van de kubus is {kubus_vol(zijde)} cm³")
print(f"De inhoud van de bol is {bol_vol(radius)} cm³")