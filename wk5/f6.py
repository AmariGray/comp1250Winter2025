
number = 1
while number <= 10:
    print(number, end="\t")
    number += 1
# sir, why don't we just use for and range()
# ANSWER: because we are working with WHILE exampls

print()

print("Working on exponentials")
number = 2
while number <= 2048:
    print(number, end="\t")
    number *= 2
print()
while True: # indeterminate/infinite loop
    number = int(input("Enter an odd number: "))
    if number % 2 == 1:
        print("Thank you for inputting an odd number")
        break
    print("Hey!", number, "is not odd")
    print("Please try again")
