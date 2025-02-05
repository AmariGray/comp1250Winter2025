"""
set is like a list
    only stores unique values
    unordered data type
    set operations
        ??? union: common values
            diff: in s1 not in s2
            symestrical_difference: not in both sets
"""

s1 = {1, 2, 3, 2, 1}
print(type(s1), s1)
# print(s1[0])  #
s1.add(11)
print(s1)
s1.discard(33)
# s1.remove(4)
l = [1,2,3,4,5,4,3]
s2 = set(l)
print(s2)
t = (8,7,5,4,3)
s3 = set(t)
print(s3)
s4 = set("benblanc")
print(s4)
s5 = set("comp1250")
l2 = list(s5)

print(s1.union(s2))
s6 = s1.union(s2)
print(s4.difference(s5))
print(s4.symmetric_difference(s5))

s7 = set(range(1,4)) # 1,2,3
s8 = set(range(0,9)) # 0,1,2,3,4,5,6,7,8
print(s7.issubset(s8))
s9 = s7.intersection(s8)
s7.difference_update(s8)  # _update = update/override s1 set values
print(s9, s7)
