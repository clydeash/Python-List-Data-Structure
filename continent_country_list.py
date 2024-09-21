countries_continents_list = ["USA - North America", "Brazil - South America", "UK - Europe", "India - Asia", "New Zealand - Oceania", "South Africa - Africa", "Russia - Europe/Asia", "China - Asia", "Canada - North America", "Mexico - North America", "Japan - Asia", "France - Europe", "Argentina - South America", "Germany - Europe", "Egypt - Africa"]

print("a. Entire list: ", countries_continents_list)
print("b. 9th index is: ", countries_continents_list[8])

countries_continents_list[9] = "Australia - Australia"
del countries_continents_list[11]

print("c. Updated list: ", countries_continents_list)
print("d. Sliced portion: ", countries_continents_list[3:8])
print("e. Last index is: ", countries_continents_list[-1])