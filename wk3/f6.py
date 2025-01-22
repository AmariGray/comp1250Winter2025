# ask the user for their student number
# what is a student number in George Brown: starts with 10 and is 9-digits

student_number = input("Enter your student number: ")

if len(student_number) == 9 and student_number.startswith("10") and student_number.isdigit():
    print("Valid Student Number")
else:
    print("Invalid Student Number")

