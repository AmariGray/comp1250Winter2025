import re

pattern = r"hello"  # regex expression
text = "text before Hello, python! Hello, hello, HeLlo! You are a cool language"

result = re.findall(pattern=pattern, string=text, flags=re.IGNORECASE)  # matches ALL occurences of a pattern of the string

print(type(result))

for hit in result:
    print(hit)
