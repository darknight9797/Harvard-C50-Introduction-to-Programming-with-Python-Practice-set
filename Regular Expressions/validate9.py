import re

email = input("Enter your email address: ").strip()

if re.search(r"^.+@.+\.edu$",email):   # ^ start of string, $ end of string
    print("Valid email address.")
else:
    print("Invalid email address.")