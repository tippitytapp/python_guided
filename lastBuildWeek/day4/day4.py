array = [1, 3, 4, 2, 2]
array2 = [3, 1, 3, 4, 2]
array3 = [10, 11, 7, 12, 4, 6, 19, 11]


def findDuplicate(nums):
    numsdict = dict()
    for num in nums:
        if num in numsdict:
            return num
        numsdict[num] = 1


print(findDuplicate(array)) # expect 2
print(findDuplicate(array2))  # expect 3
print(findDuplicate(array3)) # expect 11