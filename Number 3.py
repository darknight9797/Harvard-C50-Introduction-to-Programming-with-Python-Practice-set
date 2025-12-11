while True:         #loop for enrering an integer until valid
    try:
        x = int(input("Enter a number: "))
        break
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")   

    
    
print(f"x is {x}")       