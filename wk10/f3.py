import re

pattern = r"hello"  # regex expression
text = "text before Hello, python! Hello, hello, HeLlo! You are a cool language"

result = re.search(pattern=pattern, string=text, flags=re.IGNORECASE)  # matches the FIRST occurence of a pattern of the string

print(type(result))
if not result:  # result == None
    print("Pattern not found in string")
else:
    print(result.group())  # output the matching part of text
    print("This term was found at index", result.start(), "and ended at index", result.end())
