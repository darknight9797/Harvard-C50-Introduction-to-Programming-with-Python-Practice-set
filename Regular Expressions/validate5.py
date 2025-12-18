import re

email = input("Enter your email address: ").strip()

if re.search(".*@.*",email):    #. any character  ** ** 0 or more times repetition
    print("Valid email address.")
else:
    print("Invalid email address.")