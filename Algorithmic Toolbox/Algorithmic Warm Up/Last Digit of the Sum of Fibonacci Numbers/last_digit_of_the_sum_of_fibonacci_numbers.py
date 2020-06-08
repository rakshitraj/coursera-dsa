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

def pisano_sum(n):
    current, next = 0,1
    sum = 0
    for _ in range(n):
        current, next = next, (current+next)%10
        sum += current
    return sum%10

def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    # since the pisano period of 10 is 60
    m = int(n/60)
    sum = (m * pisano_sum(60)) + pisano_sum(((n+1) % 10))
    return sum%10

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
