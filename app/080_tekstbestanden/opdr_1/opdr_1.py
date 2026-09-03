# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

vraag1 = input("Wat vind je van de huidige regering? ")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe? ")
vraag3 = input("Wat vind jij de mooiste stad van Nederland? ")

with open ("vragen.txt", "w") as the_file:
    the_file.write(f"Wat vind je van de huidige regering? {vraag1}\n")
    the_file.write(f"Wat vind je van de Python-lessen tot nu toe? {vraag2}\n")
    the_file.write(f"Wat vind jij de mooiste stad van Nederland? {vraag3}\n")

print("Bedankt! Jouw antwoorden zijn opgeslagen in het bestand!")