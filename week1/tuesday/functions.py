# define a doubling function
# takes an integer and returns the value doubled
def double(x):
    # the keyword pass means do nothing, skip function
    return x * 2

# define a list of numbers
lis = [10, 11, 12, 13, 14]

# another list to store the doubled values
doubled = []

# call our double function on every element in the list
for x in lis:
    d = double(x)
    doubled.append(d)


print(lis)
print(doubled)


## List comprehensions
doubledagain = [double(x) for x in lis]

print(doubledagain)

# list comprehension to copy the elements of lis
# and populate another list with them
copy_of_lis = [x for x in lis]

print(copy_of_lis)
# list comprehension to only copy the even elements of lis
# and populate another list with them
evens_of_lis = [x for x in lis if x % 2 == 0]

print(evens_of_lis)