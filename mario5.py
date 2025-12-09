def main():
    print_square(3)
    
def print_square(size):
    
    #for each row in square
    for i in range(size):
        print_row(size)  #Using a helper function to print each row
        
def print_row(width):
    print("#" * width)  #Using string multiplication to print the row
    
main()