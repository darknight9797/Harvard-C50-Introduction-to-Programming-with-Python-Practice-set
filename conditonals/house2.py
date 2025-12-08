#match keyword
name = input("Enter a name: ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case "Luna":
        print("Ravenclaw")
    case "Cedric":
        print("Hufflepuff")
    case _:
        print("Who?")
