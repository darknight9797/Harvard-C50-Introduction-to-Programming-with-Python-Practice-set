import re

email = input("Enter your email address: ").strip()

if re.search(r".+@.+\.edu",email):    #\.edu at the end . \ is used to include literal dot.
    print("Valid email address.")
else:
    print("Invalid email address.")