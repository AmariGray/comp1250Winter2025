

# list method = actions on a list
# what is difference between string method and list method?
# ANSWER: a string method is executed on strings
#           a list method is executed on lists
#creating
values = []  # empty list

# adding
values.append("value1")
values.append(1234)
values.append(False)
print(values)

#modifying

values[0] = "comp1250"
values.append(3)
values.append(4)
values.append(5)
values.append(6)
values.append(7)
values.append(8)
values.append(9)
values.append(10)

values[10] = "new value"


# reading
index = 5
print(values[index * -1]) 

# deleting
values.remove(5)  # need to CHECK if value is in list
print(values)

# checking
print(7 in values)
if 5 in values:
    values.remove(5)
else:
    print(5, "is not found in the list")

if 8 in values:
    print(8, "is found in index", values.index(8))


# other functions

firstname = list("ben")
lastname = list("blanc")
print(firstname, lastname)
fullname = firstname + lastname
print(fullname)

mystery = list(range(1, 6))
print(mystery)
mystery = mystery * 3
print(mystery)

