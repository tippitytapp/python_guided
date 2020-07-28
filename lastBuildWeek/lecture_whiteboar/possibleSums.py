def recurse(coins, quantity, s, running_total):
    if quantity == [ 0 for _ in range(len(coins))]:
        return
    for i, coin in enumerate(coins):
        if quantity[i] > 0:
            quantity[i] -= 1
            running_total += coin
            s.add(running_total)
            recurse(coins, quantity, s, running_total)



def possibleSums(coins, quantity):
    unique_sums = set()
    recurse(coins, quantity, unique_sums, 0)

    # for i, coin in enumerate(coins):
    #     if quantity[i] > 0:
    #         running_total += coin
    #         quantity[i] -= 1
    #         unique_sums.add(running_total)
    return len(unique_sums)