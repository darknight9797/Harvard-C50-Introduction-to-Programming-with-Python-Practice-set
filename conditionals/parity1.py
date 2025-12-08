def main():
    x = int(input("Enter a number: "))
    if iseven(x):
        print("The number is even.")
    else:
        print("The number is odd.")

def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False

        
main()
