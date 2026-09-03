# Opdracht 2 lists
# Naam student: Vladyslav Kuchuk
# Groep: 4ITX7


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....
print("De rivier " + rivieren[0].title() + " loopt door onder " + rivier_info[rivieren[0]][1].title())

print("De rivier " + rivieren[1].title() + " loopt door onder " + rivier_info[rivieren[1]][0].title())

print("De rivier " + rivieren[2].title() + " loopt door onder " + rivier_info[rivieren[2]][2].title())