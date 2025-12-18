import re

email = input("Enter your email address: ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):   # a-zA-Z0-9_ allowed characters
    print("Valid email address.")
else:
    print("Invalid email address.")