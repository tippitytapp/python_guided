### DAY ONE CODE ###

# data = [None] * 128 # Size should be a power of 2

# def my_hash(s):
#     sb = s.encode()

#     total = 0

#     for b in sb:
#         total +=b
#         # total &= 0xffffffff
#         # total &= 0xffffffffffffffff
#     return total

# def get_index(s):
#     h = my_hash(s)
#     i = h % len(data)


#     return i

# def put(k, v):
#     # Get the index into "data" to store v
#     i = get_index(k)
#     # store v there
#     data[i] = v

# def get(k):
#     i = get_index(k)

#     return data[i]

# def delete(k):
#     i = get_index(k)

#     v = data[i]

#     data[i] = None
#     return v


# if __name__ == "__main__":

#     print(my_hash("marc"))
#     print(my_hash("goats"))
#     print(get_index("marc"))
#     print(get_index("goats"))

#     put("marc", 3490)
#     put("goat", 999)
#     put("marc", 111)

#     print(data)

#     print(get("marc"))
#     print(delete('marc'))

### DAY TWO CODE ###


data = [None] * 8 # Size should be a power of 2

def my_hash(s):
    sb = s.encode()
    total = 0
    for b in sb:
        total +=b
        # total &= 0xffffffff
        # total &= 0xffffffffffffffff
    return total

def get_index(s):
    h = my_hash(s)
    i = h % len(data)
    return i

def put(k, v):
    # Get the index into "data" to store v
    i = get_index(k)
    # store v there
    data[i] = v

def get(k):
    i = get_index(k)
    return data[i]

def delete(k):
    i = get_index(k)
    v = data[i]
    data[i] = None
    return v

if __name__ == "__main__":
    put("beej", 3490)
    put('goats', 999)

    print()