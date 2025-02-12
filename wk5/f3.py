l = list("Ben")
d1 = dict.fromkeys(l)
print(d1)

view_object_keys = d1.keys()  # a reference to X of diction
# in this case, KEYS of dictionary

#_values

vo_vals = d1.values()

d1['new_key'] = 123

print(view_object_keys)
print(list(vo_vals))
