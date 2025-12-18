import re

email = input("Enter your email address: ").strip()

if re.search("..**@..*",email):    #..* = at least two characters (any) before and after @
    print("Valid email address.")
else:
    print("Invalid email address.")