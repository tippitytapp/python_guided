# Runtime Complexity
# Algorithms

Objective = '''To define what runtime complexity is as well as enumerate some of the main Big O runtime classifications and start to understand what each one means'''

# Whats the point of runtime complexity?
# Whats the Big O>

# Some of the Main Big O Classifications -
constant_time = 'O(c)'
# The algorithm in question executes the same number of operations regardless of the size of the input
# So for any input size 'n', a constant time algorithm performs the same number of operations every time
# if you graph it out, it would be horizontal line
def print_one_item(items):
    print(items[0])

def do_a_bunch_of_stuff(items):
    last_idx = len(items) - 1
    print(items[last_idx])

    middle_idx = len(items) / 2
    idx = 0
    while idx < middle_idx:
        print(items[idx])
        idx = idx + 1

    for num in range(2000):
        print(num)

logarithmic_time = 'O(logn)'
# The algorithm in question increases the number of operations it performs as a logarthmic function of the input size n
# the function log n grows very slowly, so as n gets larger, the number of operations in the algorithm will not increase by much
linear_time = 'o(n)'
# the algorithm in question increases the number of operations it performs as a linear function of th einput size of 'n'
# The number of additional operations the algorith needs to perform grows in direct proportion to the increase in input size of 'n'

def print_every_time(items):
    for item in items:
        print(item)

def search_for_thing(items, thing):
    for item in items:
        if item == thing:
            return True
    return False

log_linear_time = 'O(nlogn)'
# The algorithm in question increases the number of operations it perfors as a log-linear function of the input size 'n'
# Intuitively you can think of this runtime classification as looking over every single element and doing some additional work on each one.
# pretty much only applied to sorting
quadratic_time = 'O(n^c)'
# the algorithm in question increases the number of operations it performs as a quadratic function of the input size n
# n = 10 => n^2 = 100
# n = 100 => n^2 = 1,000,000

def print_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)

def do_different_things(items):
    for item in items:
        print(item)
    
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)

exponential_time = 'O(c^n)'
# The algorithm in question increases the number of operations it performs as an exponential function of the input size 'n'
# For exponential problems, the number of nested loops increases as a function of the input size 'n'

static_constant = 'c'
size_on_input = 'n'


def foo(n):
    i = 1
    while i < n:
        print(i)
        i *= 2