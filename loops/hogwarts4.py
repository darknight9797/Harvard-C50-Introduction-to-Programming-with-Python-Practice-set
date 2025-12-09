# Hogwarts students and their houses stored in a dictionary

students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"}

for student in students:        
    print(student, students[student], sep = ", ")             #prints student names along with their houses (keys and values of the dictionary with a seperation of ,)
