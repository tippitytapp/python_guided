# Recursion

the_base_case = "When does the recurstion stop?"
question = "How do i move towards the base case?"

ua = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def iter_search(unsorted_array, target):
    for x in unsorted_array:
        if x == target:
            # i found the thing
            return True
    # i couldn't find the thing
    return False

def recur_search(unsorted_array, target):
    if len(unsorted_array) == 0:
        return False
    if unsorted_array[-1] == target:
        return True
    return recur_search(unsorted_array[:-1], target)


print(iter_search(ua, 4))
print(iter_search(ua, 24))
print(recur_search(ua, 3))
print(recur_search(ua, 9))
print(recur_search(ua, 23))
