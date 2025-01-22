# ask user for their firstname
# ensure name is at least 3 characters
# and has a vowel

name = input("Enter your name: ")
if len(name) >= 3 and ("e" in name.lower() or "a" in name.lower() or "i" in name.lower() or "o" in name.lower() or "u" in name.lower()):
    print(f"{name} is valid, having at least 3 chars and a vowel")
else:
    print(f"{name} is an invalid name")
