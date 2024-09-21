land_animal_speed_list = ["Lion - 80 km/h", "Gazelle - 96 km/h", "Ostrich - 70 km/h", "Fox - 48 km/h", "Wildebeest - 80 km/h", "Pronghorn - 88 km/h", "Springbok - 88 km/h", "Thomson's Gazelle - 80 km/h", "Leopard - 60 km/h", "Hyena - 60 km/h", "Zebra - 65 km/h", "Elephant - 40 km/h"]

print("a. Entire list: ", land_animal_speed_list)
print("b. 7th index is: ", land_animal_speed_list[6])
land_animal_speed_list[8] = "Cheetah - 120 km/h"
del land_animal_speed_list[9]
print("c. Updated list: ", land_animal_speed_list)
print("d. Sliced portion: ", land_animal_speed_list[2:7])
print("e. Last index is: ", land_animal_speed_list[-1])