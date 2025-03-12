import re

name = input("Enter your name").strip()

pattern = r"[a-z]+"

match = re.match(pattern=pattern, string=name, flags=re.IGNORECASE)

if match and (match.start() + match.end()) == len(name):
    print(name, "is a valid name")
else:
    print("Sorry, but that name is invalid")
