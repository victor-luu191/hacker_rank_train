import bisect

# TODO: recurrent solution exceed recursion depth, inspect later
def recurMaximumToys(prices, k):
    # greedy: often we start with the toy with smallest price, so that have more money left, can buy more.
    # Also, prices larger than k can be excluded right away
    # exclude prices larger than k to reduce redundant computation
    index = bisect.bisect_right(prices, k)
    valid_prices = prices[:index]

    # stop condition
    if not valid_prices:  # no valid toys to buy
        return 0

    cheapest = valid_prices[0]
    print('cheapest price: ', cheapest)
    if cheapest > k:  # can buy nothing as not enough money to buy even the cheapest toy
        return 0
    else:  # buy the cheapest, then find out how many can be bought with remaining money
        remain = k - cheapest
        print('remain money: ', remain)
        return 1 + recurMaximumToys(valid_prices[1:], remain)  # exclude the cheapest toy as cannot buy dups