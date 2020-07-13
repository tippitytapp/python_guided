# Linked List vs. Arrays

# RAM

# _____________________________________________________________________________
# |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
  # 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18
          #   [ 1,  2,  3,  4 ]
# arr = [1, 2, 3, 4] => must be in the same order in RAM

# LL can be anywhere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# _____________________________________________________________________________
# |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
  # 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18
  #    LL1 LL2  A1  A2  A3  A4 LL3 LL4 LL5 LL6  A1  A2  LL7 LL8 A1  A2  LL9 LL0 

array = [1, 2, 3, 4, 5, 6, 7]

print('array', array)
# O(1)
array.pop()
print('pop' , array)
# O(n)
array.pop(0)
print('pop(0)', array)
# O(n)
array.pop(2)
print('pop(2)', array)
array.insert(0, 0)
print('insert(0, 0)', array)


LinkedList = list()

# remove_from_tail