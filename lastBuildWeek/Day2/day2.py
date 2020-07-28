numsArray = [2, 7, 11, 15]
numsArray2 = [3, 2, 4]
numsArray3 = [3,3]
tgt = 9
tgt2 = 6 

def twoSum(nums, target):
    i = 0
    j = i + 1
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[i] + nums[j] == target:
                return [i, j]


                
print(twoSum(numsArray, tgt))
print(twoSum(numsArray2, tgt2))
print(twoSum(numsArray3, tgt2))

# ############################################################################################################
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = list()
        self.length = 0
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.storage.append(x)
        self.length += 1
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        popped = self.storage.pop(0)
        self.length -=1
        return popped

    def peek(self) -> int:
        """
        Get the front element.
        """
        peeked = self.storage[0]
        return peeked

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.length == 0:
            return True
        else:
            return False

# #############################################################################################################

strsArray = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):
    newstrs = dict()
    response = list()
    for string in strs:
        newString = "".join(sorted(string))
        if newString not in newstrs:
            newstrs[newString] = [string]
        else:
            newstrs[newString].append(string)
    for key, value in newstrs.items():
        response.append(value)
    return response
    

print(groupAnagrams(strsArray))