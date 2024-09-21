pokemon_names = ["Bulbasaur", "Charmander", "Squirtle", "Eevee", "Jigglypuff", "Snorlax", "Mewtwo", "Articuno", "Zapdos", "Moltres", "Chikorita", "Cyndaquil", "Totodile", "Lugia", "Ho-oh", "Treecko", "Torchic"]

print("a. Entire list: ",pokemon_names)
print("b. 9th index is : ", pokemon_names[9])
pokemon_names[12] = "Pikachu"
del pokemon_names[10]
print("c. Updated list: ",pokemon_names)
print("d. Sliced portion: ", pokemon_names[4:7])
print("e. Last index is: ", pokemon_names[-1])