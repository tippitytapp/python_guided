import math
import os
import random
import re
import sys

def twoStrings(s1, s2):
                            # Runtime: O( n + m )
    s = set()               # O(1)

    for char in s1:         # O(n)
        s.add(char)         # O(1)

    for char in s2:         # O(n)
        if char in s:       # O(1)
            return 'YES'
    return 'NO'

                            # Runtime: O ( n * m ) - O(n^2)
    # for char in s1:       # O(n)
    #     if char in s2:    # O(m)
    #         return 'YES'
    # return 'NO'

print(twoStrings('Hello', 'World'))