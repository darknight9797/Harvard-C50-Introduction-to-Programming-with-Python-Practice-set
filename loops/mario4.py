def main():
    print_square(3)
    
def print_square(size):
    
    #for each row in square
    for i in range(size):
        print("#" * size)  #Using string multiplication to print each row
main()
