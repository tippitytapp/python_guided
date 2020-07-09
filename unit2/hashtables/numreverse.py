# cache = {}

# def build_lookup_table():
    # for i in range(1000):
    #     cache[i] = num_reverse(1)

# def num_reverse(n):
#     if n in cache:
#         return cache[n]

#     n2 = list(str(n))
#     n2.reverse()
#     n2 = ''.join(n2)
#     cache[n] = int(n2)
#     return cache[n]

# build_lookup_table()
# print(num_reverse(123))

class NumReverser:
    def __init__(self):
        self.cache = {}
        for i in range(1000):
            self.cache[i] = self.num_reverse(i)

    def num_reverse(self, n):
        if n in self.cache:
            print('cache hit', self.cache[n])
            return self.cache[n]

        n2 = list(str(n))
        n2.reverse()
        n2 = ''.join(n2)
        self.cache[n] = int(n2)
        return self.cache[n]

nr = NumReverser()
print(nr.num_reverse(123))
