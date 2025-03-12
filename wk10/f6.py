import re
# ask the user to input their DOB (date of birth)
# in the format of YYYY-MM-DD
# take user input & Validate

dob = input("Enter your date of birth in format YYYY-MM-DD: ")

pattern1 = r"\d{4}-\d{2}-\d{2}"

result = re.match(pattern=pattern1, string=dob)
if result:
    parts = result.group().split("-")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[1])

    if year <= 2025 and month >= 1 and month <= 12 and day >= 1 and day <=31:
        print("Your DOB is valid")
        print("Your DOB is", result.group())
    else:
        print("Invalid DOB")
else:
    print("Invalid DOB")
