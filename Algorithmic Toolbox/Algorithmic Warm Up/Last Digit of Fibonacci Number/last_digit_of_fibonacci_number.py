# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    # Implementing property of Pisano Period
    current, next = 0,1
    # since the first iteration is already handled during initialization
    # the range function will remove the the last iteration to compensate
    for _ in range(n):
        current, next = next, (current+next)%10
    return current


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
