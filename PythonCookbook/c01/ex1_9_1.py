a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find keys in common
a1 = a.keys() & b.keys() #{'x', 'y'}

# Find keys in a that are not in b
a2 = a.keys() - b.keys() # {'z'}

# Find (key, value) pairs in common
a3 = a.items() & b.items() # {('y', 2)}

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}
print(a1)
print(a2)
print(a3)
print(c)
