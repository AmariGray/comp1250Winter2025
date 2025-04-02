"""
Determine what is the next value in sequence
    example: if the number inputs a number
             the next value should be number + 1

             if the user inputs a letter
             the next value should be the following letter


Question 1a) Do we need input from the user?
            ANS: yes
        1b) Does this input come from input() or a function parameter

Question 2) What are the variables that I need to set up?
                Three categories:
                    Category 1: initial values
                                    info from user/function params
                    Category 2:
                                    processing values
                                        conversion
                                        manipulate
                    Category 3: final product/result
Question 3) Do we need to make decisions in the program?
            ANS: YES
                decisions are made in the processing phase
                categories of decisions
                    decision trees (if statments)
                    validate data => not raise an error
                    which data type to use
                        single value
                            is value numerical
                                is value decimal
                                    float
                                int
                            string
                        then choose from a collection data type
                            list, set, tuple, dictionary, etc
"""
import sys

# initial variable
user_data = input("Enter a number or a letter")
# processing value(s)
value_to_increase_by = 1

# processing value(s)
if user_data.isdigit():
    converted = int(user_data)
    # final product/result
    next_value = converted + 1
else:
    # how do we determine the next letter of a text
    # Step 1: get only the first letter
    first_letter = user_data[0].lower()  # work with lower case
    # Step 2: ensure that the user only put letters a-z
    # 26 if statements
    # convert letter into a number, determine if that number is within
    letter_as_number = ord(first_letter)
    if letter_as_number >= 97 and letter_as_number <= 122:
        print(first_letter, "is within range of A-Z")
        letter_as_number += value_to_increase_by
        next_value = chr(letter_as_number)
        user_data = user_data[0].lower()
    else:
        print("Invalid input. The input was neither a number nor a letter", file=sys.stderr)


print("The next value after", user_data, "is", next_value)
