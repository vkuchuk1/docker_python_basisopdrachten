# Opdracht 2 tekstbestanden
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)
nul = 0
while True:
    print(prompt)
    userprompt = input()
    nul += 1
    if int(userprompt) < geheim_getal:
        print("Hoger")
    elif int(userprompt) > geheim_getal:
        print("Lager")
    else:
        print("Gefeliciteerd! Je hebt het geheime getal geraden!")
        print(f"Aantal pogingen: {nul}")
        break