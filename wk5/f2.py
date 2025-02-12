"""
dictionary
    key-value pair

"""

d1 = dict()
d2 = {}  # What gives?!
print(type(d1), type(d2))
d3 = {
    "name": "Ben",
    "age": 20,
    "weight": 155.5
}
s1 = {"Ben", 20, 155.5}
s2 = {"name", "age", "weight"}

print(d3["name"])  # Ben
print(d3['age'])  # 20

d3['grade'] = 100
d3['card_collection'] = {"NBA", "NFL", "NHL"}
d3['fav_foods'] = ["hot dog", "hamburger", "pizza"]
print(d3['card_collection'])
print(d3['fav_foods'][1])  # ???

d3['fav_foods'].remove('pizza')  # ??? legal?
d3['grade'] = 101

del d3['card_collection']  # remove key and value
d3.popitem() # remove last insert value
d3.pop("name")  # removes item based on key
print(d3)
