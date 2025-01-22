name = input("Enter your name in the format of lastname,firstname: ")

if "," in name:
    print("Thank you for following the format")
    names = name.split(",")  # a list. index/indexes
    #blanc,ben
    lastname = names[0]
    firstname = names[1]
    print(f"Your firstname is {firstname}. Your lastname is {lastname}")
else:
    print("Incorrect input")