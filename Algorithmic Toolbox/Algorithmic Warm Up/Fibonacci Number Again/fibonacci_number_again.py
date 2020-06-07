# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

# Lists the pisano period
def pisano(m):
    pisano: List[int] = [0]
    previous, current = 0, 1
    while True:
        previous, current = current, (previous + current) % m
        pisano_period.append(previous)
        if previous == 1 and current == 0:
            break
        return pisano

# Gives the length of Pisano period
def pisano_period(m):
    current, next = 0, 1
    period = 0

    while True:
        current, next = next, (current + next) % m
        period += 1
        if current == 0 and next == 1:
            return period


def fib_mod(n, m):
    current, next = 0, 1
    for _ in range(n):
        current, next = next, (current + next) % m

    return current

def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    return fib_mod(n % pisano_period(m), m)

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
