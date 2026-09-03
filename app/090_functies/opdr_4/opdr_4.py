# Opdracht 1 functies
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7


def volledige_naam(namen):
    for naam in namen:
        volledige_naam = naam["voornaam"] + naam["tussenvoegsel"] + naam["achternaam"]
        print(volledige_naam.strip())


namen = [
    {"voornaam": "Willem", "tussenvoegsel": " van ", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": " ", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": " van der ", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": " ", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)