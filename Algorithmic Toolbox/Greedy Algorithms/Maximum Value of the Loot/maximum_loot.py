# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    saffron = prices[0]/weights[0]
    vanilla = prices[1]/weights[1]
    cinnamon = prices[2]/weights[2]

    while capacity:
        if cinnamon > saffron and cinnamon > vanilla:
            u3 = min(capacity, 5)
            capacity -= u3
            cinnamon = 0
        elif saffron > vanilla and saffron > cinnamon:
            u1 = min(capacity,4)
            capacity -= u1
            saffron = 0
        elif vanilla > saffron and vanilla > cinnamon:
            u2 = min(capacity, 3)
            capacity -= u2
            vanilla = 0
    loot = (u1*price[0]) + (u2*price[1]) + (u3*price[2])
    return loot


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
