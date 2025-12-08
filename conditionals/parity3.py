#use this version to define iseven function and call it from main, also made the function more compact

def main():
    x = int(input("Enter a number: "))
    if iseven(x):
        print("The number is even.")
    else:
        print("The number is odd.")

def iseven(n):
   return n % 2 == 0                                #compact form OF if n % 2 == 0:
                                                                         # return True
                                                                    # else:
                                                                     #   return False


        
main()
