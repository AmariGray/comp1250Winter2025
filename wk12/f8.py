"""
Goal is to create the following csv file using python code

Student ID,Name,Age
1000,John,20
2000,Mary,21
3000,Sally,22
"""

headers = "Student ID,Name,Age".split(",")  # list of 3 values

data = [
    "1000,John,20".split(","),
    "2000,Mary,21".split(","),
    "3000,Sally,22".split(","),
]
print(headers)
print(data)

with open("c2.csv", "w") as fo:
    fo.writelines(",".join(headers) + "\n")
    for row in data:
        fo.writelines(",".join(row) + '\n')
