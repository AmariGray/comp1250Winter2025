# ask user for number
# determine if number is odd, even or neutral

num = int(input("Enter a number: "))

if num % 2 == 1:
    print(num, "is odd")
elif num == 0:
    print(f"{num} is neutral")
    s = f"{num} is neutral"
    print(s)
    print(num, "is neutral")
    print(str(num) + " is neutral")
else:
    print(f"{num} is even")
