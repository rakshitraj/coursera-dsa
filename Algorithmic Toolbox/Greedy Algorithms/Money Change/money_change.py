# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    coins = 0
    for denomination in [10, 5, 1] :
        new_coins = int(money/denomination)
        money = money % denomination
        coins += new_coins
    return coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
