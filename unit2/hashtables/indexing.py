# indexing
#
# What are all the employees in a certain department?

records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]



'''
# Naive
dept = input('Enter department:')
for r in records:
    if r[1] == dept:
        print(r)
'''

index = {}

def build_index():
    for r in records:
        dept = r[1]

        if dept not in index:
            index[dept] = []
        index[dept].append(r)

build_index()

while True:
    dept = input("Enter department:")
    print(index[dept])
