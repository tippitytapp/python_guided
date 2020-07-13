def find_smallest_missing(arr):
# '''    edge case: deal witht e edge case where 0 is missing
#     check to make sure that 0 is at tge front of the array
#     edge case: if no elements are missing, return the element right 
#     after the last element

#     loop through the arr
#     check adjacent elements
#     # make sure that the adjacent element == currnent + 1
#     current = arr[0]
# '''

    ### SOLUTION # 1
    if len(arr) == 0:
        return
    if arr[0] != 0:
        return 0
    for i in range(len(arr) - 1):
        if arr[i+1] != arr[i]+1:
            return arr[i] + 1
    return arr[-1] + 1

    ### SECOND SOLUTION
    # pass

# INPUT ARRAYS
a = [0, 1, 2, 6, 9, 11, 15] # smallest missing is 3
b = [1, 2, 3, 4, 6, 9, 11, 15] # smallest missing is 0
c = [0, 1, 2, 3, 4, 5, 6] # smallest missing is 7
d = []
print('fsm', find_smallest_missing(a))
print('fsm', find_smallest_missing(b))
print('fsm', find_smallest_missing(c))
print('fsm', find_smallest_missing(d))



# in a singly linked list context
def find_middle_of_linked_list(ll):
    # get the length of the length list
    # once we know the length, we can calulate the midpoint
    # of that length
    # traverse to that midpoint node
    length = len(ll)
    mid = length // 2
    return ll[mid].value

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next       

    def __str__(self):
        return f'{self.value}'
sll = []

root = Node(3)
root.next = Node(4)
root.next.next = Node(5)
root.next.next.next = Node(6)
root.next.next.next.next = Node(7)
sll.append(root)
sll.append(root.next)
sll.append(root.next.next)
sll.append(root.next.next.next)
sll.append(root.next.next.next.next)


print('fmoll', find_middle_of_linked_list(sll) )
