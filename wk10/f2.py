import re

pattern = r"hello"  # regex expression
text = "Hello, python! You are a cool language"

result = re.match(pattern=pattern, string=text, flags=re.IGNORECASE)  # matches a pattern starting at the START of the string

print(type(result))

if not result:  # result == None
    print("Pattern not found in string")
else:
    print(result.group())  # output the matching part of text