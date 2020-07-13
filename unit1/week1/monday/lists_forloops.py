# lists === arrays

# create an empty list
# set to varible p
p = []

# create a list with numbers
q = [1, 2, 3, 4, 5, 6] # [1, 2, 3, 4, 5, 6]

# add a number to our q list
q.append(77)

# where the appended value getting added to the list?

print(q) # [1, 2, 3, 4, 5, 6, 77]

# what if we want to add to the beginning of the list

q.insert(0, 90)

print(q) # [90, 1, 2, 3, 4, 5, 6, 77]

# how to print out all the elements of a list
# use a for loop to do this
for element in q:
    print(element)


# combine above loop with string interpolations

for element in q:
    print(f'Element: {element}')

# print each list element with a short message that also tells us the elements index

for index, element in enumerate(q):
    print(f'Index: {index}, Element: {element}')

# In Python, how do we loop just a certain number of times?
# we can use the range function 
# range(start = 0, end, step=1 )
# range(10), assumes start-0
for elem in range(0, 10):
    print(elem)

for elem in range(2, 10):
    print(elem)

for elem in range(5, 100, 10):
    print(elem)

# use range in conjunction with lists to iterate over the length of an array

for index in range(0, len(q)):
    print(q[index])

# how do you loop through a range backwards

for i in range(10, 0, -1):
    print(i)

# how can i loop past the end of a list?

for i in range(20):
    if i< len(q):
        print(q[i])
    else:
        print(i)

