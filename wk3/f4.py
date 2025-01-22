# ask the use for their age
# output whether or not they are
# a child, a teenager, an adult or an elderly person
# child: 0-12
# teenage: 13-17
# adult: 18-64
# elderly: 65+
age = int(input("Enter your age: "))

if age < 0 or age > 100:
    print("Invalid age")
else:
    if age >= 0 and age <= 12:
        print("You are a child")
    elif age >= 13 and age <= 17:
        print("you are a teenager")
    elif age >= 18 and age <= 64:
        print("You are an adult")
    else:
        print("You are an elderly person")
