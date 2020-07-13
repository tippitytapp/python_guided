# BINARY AND LINEAR SEARCHES

def linear_serch(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
        return -1
        # RUNTIME IS O(n)

def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        middle = (low+high) / 2
        if target < arr[middle]:
            high = middle -1
        elif target > arr[middle]:
            low = middle+1
        else:
            return middle
        return -1
        # RUNTIME IS O(log(n))



## ITERATIVE SORTING

our_numbers = [5,9,3,6,2,1,7,8,4]

def selection_sort(items):
    for i in range(0, len(items) -1):
        cur_index = i
        small_index = cur_index
        for j in range(cur_index +1, len(items)):
            if items[j] < items[small_index]:
                small_index = j

        items[small_index], items[cur_index] = items[cur_index], items[small_index]
    return items

print("original array", our_numbers)
print("sorted array", selection_sort(our_numbers))