"""
loops
    aka cycles
        3 components
            start
            end
            update (progression from start to end)

        2 loops: for and while
            for: iterate a collection (list, tuple, set,dictionary, etc)
            while: iterate based on condition (boolean expression)

        for placeholder_name in collection
"""

for letter in "comp1250":
    print(letter, end=" ")
print()

items = ["cool", "examples", "using", "python", 1, 1.23, True]

for each_value in items:
    print(each_value, end='\t')
print()
for val in {1,2,3,4,3,2,1}:
    print(val, end="\t")
""
d1 = {"name": "Intro to Programming", "code": 1250,
      "lecture_day": "Wednesday", "lecture_time": 8.0}
print()
for mystery in d1.items():  # .keys(), .values(), .items()
    print(mystery, end='\t')
    print(mystery[0], mystery[1], end='\t')
    print(d1[mystery[0]])