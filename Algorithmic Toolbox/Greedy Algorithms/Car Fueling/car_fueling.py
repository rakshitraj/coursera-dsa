# python3

def car_fueling(dist,miles,n,gas_stations):
    num_refill, curr_refill, limit = 0,0,miles
    while limit < dist:  # While the destination cannot be reached with current fuel
        if curr_refill >= n or gas_stations[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1
        # Find the furthest gas station we can reach
        while curr_refill < n-1 and gas_stations[curr_refill+1] <= limit:
            curr_refill += 1
        num_refill += 1  # Stop to tank
        limit = gas_stations[curr_refill] + miles  # Fill up the tank
        curr_refill += 1
    return num_refill

def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    return car_fueling(d, m, len(stops), stops)
    # stops.insert(len(stops), d)
    # numRefill, currentRefill, pos = 0,0,0
    # while currentRefill < len(stops) -1 :
    #     if stops[currentRefill] - pos > m:
    #         return -1
    #     lastRefill = currentRefill
    #     while (currentRefill < len(stops) -1 and
    #            stops[currentRefill + 1] - stops[lastRefill] <= m ) :
    #         currentRefill += 1
    #     numRefill += 1
    #     pos = stops[currentRefill]

    return numRefill

if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
