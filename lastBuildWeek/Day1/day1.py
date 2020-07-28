array1 = [1, 2, 3, 1]
array2 = [1, 2, 3, 4]
array3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
array4 = []
array5 = [2, 14, 18, 22, 22]

def contains_duplicates(nums):
    newnums = set()
    if len(nums) == 0:
        return False
    for num in nums:
        if num in newnums:
            return True
        newnums.add(num)
    return False

print(contains_duplicates(array1)) # Should print true
print(contains_duplicates(array2)) # should print false
print(contains_duplicates(array3)) # should print true
print(contains_duplicates(array4)) # should print false
print(contains_duplicates(array5)) # should print true

###############################################################################################

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def add_two_numberss(l1, l2):
    # list1 = list()
    # list2 = list()

    # if l1.val is not None:
    #     list1.append(str(l1.val))
    #     while l1.next is not None:
    #         list1.append(str(l1.next.val))
    #         l1 = l1.next
    # if l2.val is not None:
    #     list2.append(str(l2.val))
    #     while l2.next is not None:
    #         list2.append(str(l2.next.val))
    #         l2 = l2.next
    # reversedone = list(reversed(list1))
    # reversedtwo = list(reversed(list2))
    # # print(reversedone)
    # # string1 = "".join(reversedone)
    # # string2 = "".join(reversedtwo)
    # num1 = int("".join(reversedone))
    # num2 = int("".join(reversedtwo))
    # total = num1 + num2
    # totalstr = str(total)
    # totallist = [num for num in totalstr]
    # newlist = []
    # for i in reversed(totallist):
    #     newlist.append(ListNode(int(i))
    pass
######################################################################################

def detectCycle(self, head)
    current = head 
    
    while current is not None and current.next is not None:
        if hasattr(current, 'visited'):
            return current
        
        current.visited = True
        current = current.next 
    return