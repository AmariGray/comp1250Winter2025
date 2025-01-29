
# what are tuples: lists that are IMMUTABLE => cannot change after being created

values = ("hi", True, 98, 54.32)
print(values)

print(values[0], values[-1])

print(98 in values)

print(values.index(True))

values1 = tuple("Ben")  # ("B", "e", "n")

vals = values1 + values 
print(vals)

vals1 = vals * 3
print(vals1)


# unpack a tuple

first_letter, second_letter, third_letter = values1
print(first_letter, second_letter, third_letter)




###########################################



"""
C   O   M   P   1   2   5   0

0   1   2   3   4   5   6   7
-8  -7  -6  -5  -4  -3  -2  -1  
"""

course = list("comp1250".upper())
print(course)
print(course[2:6])  # list slicing      => sub list

print(course[:4])  # list slicing => first four

print(course[4 * -1:]) # list clicing => last four

print(course[::2])  # C M   1   5
# [{start def val of 0} : {end def val of len() or 0} : {skip def val of 1}]

del course[0]  
print(course)
