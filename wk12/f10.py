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

import csv
with open("c3.csv", "r") as fo:
    # reader or write
    reader = csv.reader(fo, delimiter=',', lineterminator='\n')
    for row in reader:
        print(row)

