music_genre_list = ["Pop", "Rock", "Hip Hop", "R&B", "Country", "Electronic", "Classical", "Reggae", "Blues", "Disco", "Funk", "Metal", "Soul", "Indie", "Reggaeton"]

print("a. Entire list: ", music_genre_list)
print("b. 10th index is: ", music_genre_list[10])
music_genre_list[4] = "Jazz"
del music_genre_list[7]
print("c. Updated list: ", music_genre_list)
print("d. Sliced portion: ", music_genre_list[3:8])
print("e. Last index is: ", music_genre_list[-1])