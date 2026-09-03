# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


gegevens = {"voornaam": (), "achternaam": (), "drank": (), "eten": ()}
vragen = ["Wat is je voornaam? ", "Wat is je achternaam? ", "Wat neem je mee aan drank? ", "Wat neem je mee om te eten? "]

gegevens["voornaam"] = input(f"1. {vragen[0]}")
gegevens["achternaam"] = input(f"2. {vragen[1]}")
gegevens["drank"] = input(f"3. {vragen[2]}")
gegevens["eten"] = input(f"4. {vragen[3]}")

print("Bedankt voor het invullen! \n" "See you at the party.")

with open ("party.txt", "a") as the_file:
    the_file.write(f"Voornaam: {gegevens['voornaam']}\n")
    the_file.write(f"Achternaam: {gegevens['achternaam']}\n")
    the_file.write(f"Drank: {gegevens['drank']}\n")
    the_file.write(f"Eten: {gegevens['eten']}\n")