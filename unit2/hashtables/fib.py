# 0 1 1 2 3 5 8 13 21
# Memoization, caching

def fib(n):
    cache = {}
    def fib_inner(n):
        if n <= 1:
            return n
        if n not in cache:
            cache[n] = fib_inner(n-1) + fib_inner(n-2)
        return cache[n]
    return fib_inner(n)



for i in range(100):
    print(f'{i}: {fib(i)}')
