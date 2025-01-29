#implicit: behaves like list but not list => strings
#explict: is a list data type

print(type("hello"))

greeting = list("Hello")
print(type(greeting))
print(greeting)

"""
H           e           l           l       o

0           1           2           3       4
-5          -4          -3          -2      -1

"""
print(greeting[-4], greeting[1])

