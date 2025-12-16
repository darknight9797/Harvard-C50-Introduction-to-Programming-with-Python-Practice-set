with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")    #name = row[0], house = row[1]
        print(f"{name} is in {house}")