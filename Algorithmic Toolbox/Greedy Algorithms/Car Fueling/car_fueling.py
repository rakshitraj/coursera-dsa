# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    stops.insert(0,0)
    stops.insert((len(stops)),d)
    numRefills = 0
    currentRefill = 0
    while (currentRefill < len(stops) ):
        lastRefill = currentRefill
        while (currentRefill < len(stops) and
        stops[currentRefill+1] - stops[lastRefill] <= m):
            currentRefill = currentRefill+1
        if currentRefill == lastRefill:
            return -1
        if currentRefill < len(stops) :
            numRefills = numRefills + 1
        return numRefills

if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
