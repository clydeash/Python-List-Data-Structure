bird_species_list = ["Sparrow", "Robin", "Blue Jay", "Cardinal", "Hummingbird", "Owl", "Crow", "Penguin", "Parrot", "Flamingo", "Pelican", "Hawk"]

print("a. Entire list: ", bird_species_list)
print("b. 9th index is: ", bird_species_list[8])

bird_species_list[5] = "Eagle"
del bird_species_list[7]

print("c. Updated list: ", bird_species_list)
print("d. Sliced portion: ", bird_species_list[2:7])
print("e. Last index is: ", bird_species_list[-1])