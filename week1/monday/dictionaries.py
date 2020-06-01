# Dictionaries are pythons version of Objects in JS
# Useful for storing key-value pairs
# Dictionaries are immutable

# init an empty dictionary
d = {}

# create a dict with 2 key value pairs

e={"foo": 12, 16: "bar"}

# note for JS users: there is no dot notation for accessing
# dicts in Python
print(e["foo"])

print(e[16])

# loop through keys and dicts option 1
for key in e:
    print(key, e[key])

# loop through keys and value option 2
for key, val in e.items():
    print(key, val)