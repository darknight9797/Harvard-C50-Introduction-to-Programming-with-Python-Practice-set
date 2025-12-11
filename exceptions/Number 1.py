try:
    x = int(input("Enter a number: "))
       
except ValueError:
    print("Invalid input. Please enter a valid integer.")   

else:
     print(f"x is {x}")
