school_subject_list = ["Philosophy", "Science", "History", "English", "Art", "Music", "Physical Education", "Geography", "Biology", "Chemistry", "Computer Science", "Spanish"]

print("a. Entire list: ", school_subject_list)
print("b. 6th index is: ", school_subject_list[5])

school_subject_list[7] = "Mathematics"
del school_subject_list[3]

print("c. Updated list: ", school_subject_list)
print("d. Sliced portion: ", school_subject_list[2:6])
print("e. Last index is: ", school_subject_list[-1])
