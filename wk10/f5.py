import re
phone_number = input("Enter your phone number")

pattern1 = r"[^\d]"

filtered = re.sub(pattern1, "", phone_number)
print(filtered)