# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10

def pisano_period_sum():
    m = 10;
    current, next = 0, 1
    sum = 0
    period = 0
    while True:
        current, next = next, (current+next) % m
        sum += current
        period += 1
        if current == 1 and next == 0 :
            return sum, period

def sumof(m):
    current, next = 0, 1
    sum = 0
    for _ in range(m):
        current, next = next, (current+next) % 10
        sum += current
    return sum

def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    sum, period = pisano_period_sum()
    mul = (int)(n/period)
    digit = ((mul * sum) + sumof(( n % period )))%10
    return digit


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
