# slices

q = [10, 20, 30, 40, 50, 60]

# in js slice(2, 4)

# Python has a really nice slicing syntax
# if we want 3, 4 from q

print(q[2:4])

# we can leave the left side of the colon out if we want to start from 
# the beginning

print(q[:4])

print(q[4:])

# we can combine this slicing syntax with our loops
# we can use the slice function like below

for elem in q[:4]:
    print(elem)

for elem in q[4:]:
    print(elem)