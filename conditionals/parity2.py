#use this version to define iseven function and call it from main

def main():
    x = int(input("Enter a number: "))
    if iseven(x):
        print("The number is even.")
    else:
        print("The number is odd.")

def iseven(n):
   return True if n % 2 == 0 else False #compact form

        
main()
