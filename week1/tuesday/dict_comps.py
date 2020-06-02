names_and_ages = [
    ("Sarah", 22),
    ("jorge", 50),
    ("sam", 38),
    ("frank", 27),
    ("bob", 39),
    ("sandy", 46),
    ("shawn", 16)
]

for name, age in names_and_ages:
    print(name, age)

d={}
for name, age in names_and_ages:
    d[name] = age

print(d)

e = {name: age for name, age in names_and_ages}
print(e)