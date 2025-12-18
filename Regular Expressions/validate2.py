email = input("Enter your email address: ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid email address.")
else:
    print("Invalid email address. Please ensure it has a username and a valid domain.")