d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

items = list(d.items())

# print(items)
# sort ascending by key
items.sort()
# print(items)
print('')
print('sorted ascending normal')
for i in items:
    print(f'{i[0]}: {i[1]}')
print(' ')
# items.sort(reverse=True)

# print(items)

# sort ascending by value
def keyfunc(e):
    return e[1]

items.sort(key=keyfunc)
print('sorted by value')
for i in items:
    print(f'{i[0]}: {i[1]}')
print('')
items.sort(key=lambda e: e[1])
print('sorted with lambda')
for i in items:
    print(f'{i[0]}: {i[1]}')