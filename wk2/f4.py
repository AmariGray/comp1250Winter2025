# global methods of python
# global method: a function (an action) that you call to do something

# print()
print()  # prints blank line
print("hello")
print(1)
print(1.1)
print(True, False)
print("value 1", 123, -987, 45.67)
print("This line ends in an exclamation mark", end="! ")
print("follow-up text")
print("repeat text N many times. " * 5)
print("value1", "value2", "value3", 12345, 98.76, sep="--")
print("what", "does", "this", "output", sep="**", end="? ")
#what**does**this**output?

print("\n" * 3)
print("-" * 50)
value = input() # gets user input => save as string data type
print("The value inputted was", value)
value1 = input("Enter something: ")

print("\n" * 3)
print("-" * 50)
# converting to specified data types
v1 = "123"

v2 = int(v1)
v3 = float(v2)
v4 = str(v3)
v5 = bool(v4)  # if string or value is empty or 0 => False else True
v6 = bool("")
print(v1, v2, v3, v4, v5, v6)

print("\n" * 3)
print("-" * 50)

n1 = 123.46789
n2 = round(n1, 2)
print(n2)
print(round(124.65, 1))