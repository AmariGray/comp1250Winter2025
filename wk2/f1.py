# ask the user for their birth year
# create a variable for the current year
# ask the user for their name
# output the users age in
# years, months & days

# data type = type of data stored
# text, numbers (whole + decimals)
# text => string
# whole numbers => int
# decimal numbers => float

birth_year = input("In what year were you born? ")
print(type(birth_year))
birth_year = int(birth_year)
print(type(birth_year))
current_year = 2025
name = input("What is your name? ")

print("Hello", name, "you are", current_year - birth_year,
      "years old")
print("In months, you are", (current_year - birth_year) * 12)
print("In days, you are ", (current_year - birth_year) * 365.25)
