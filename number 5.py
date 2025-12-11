#using functions to handle exceptions

def main():
    x = get_integer()
    print(f"x is {x}")
    
def get_integer():
    
    while True:         #loop for enrering an integer until valid
        try:
            return int(input("Enter a number: "))
            
        except ValueError:
            print("Invalid input. Please enter a valid integer.")   

           



main()