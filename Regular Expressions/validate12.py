import re

email = input("Enter your email address: ").strip()

if re.search(r"^\w+@\w+\.edu$",email):   # \w : a-zA-Z0-9_ 
    print("Valid email address.")
else:
    print("Invalid email address.")