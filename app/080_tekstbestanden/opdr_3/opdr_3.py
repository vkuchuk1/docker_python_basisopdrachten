# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:



text = input("Voer een tekst in: ")
alfabet = "abcdefghijklmnopqrstuvwxyz"
out_alfabet = alfabet[5:] + alfabet[:5]

trans_table = str.maketrans(alfabet, out_alfabet)
result = text.translate(trans_table)
print(result)