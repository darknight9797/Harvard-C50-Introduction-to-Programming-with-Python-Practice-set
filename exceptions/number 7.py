#using functions to handle exceptions

def main():
    x = get_integer("What is x? ")
    print(f"x is {x}")
    
def get_integer(prompt):
    
    while True:         #loop for enrering an integer until valid
        try:
            return int(input(prompt))
            
        except ValueError:
            pass    #ignore the exception and loop again
           



main()
