# Opdracht 1 functies
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7


def kilometers_naar_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

def miles_naar_kilometers(miles):
    kilometers = miles / 0.621371
    return kilometers

kilometers = 1223
miles = 867

print(f"{kilometers} kilometers is {kilometers_naar_miles(kilometers)} miles")
print(f"{miles} miles is {miles_naar_kilometers(miles)} kilometers")