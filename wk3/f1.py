t1 = "ben blanc"
t2 = "Ben Blanc"

print(t1 == t2)  # boolean expression
# A boolean expression
# is an expression that results
# in True or False (boolean value)
# involves relational operator
# ==, !=, <, >, <=, >=
# FYI: for strings, can only
# use ==, !=
# for numbers, can use all relational operators

print(t1 != t2)
print(not t1 == t2)
print(t1.lower() == t2.lower())

# a string method: an action
# on a string
# syntax? string variable or value dot method name
print("hello".upper())
print("ben blanc".title())
print(t1.title())
print(t2.lower().count("b"))
print(t2.lower().count("bl") >= 1)
print("    ben blanc    ")
print("    ben blanc    ".strip())
print(t1.title().ljust(20, '*'))
print(t1.title().rjust(20, '*'))
print(t1.title().center(20, '*'))
print(t1.find("bl"))  # index of text
print("e" in t1)

saved = t1.title()

print(t1.replace(" ", "").isalpha())
print(t1.replace(" ", "").isalnum())
print("12345".isdigit())
print(len(t1), len(t2), len(t1.replace(" ", '')))
