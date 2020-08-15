# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    k=0
    while n>k:
        k += 1
        n -= k
        if n>k :
            summands.append(k)
        else :
            summands.append(n+k)

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
