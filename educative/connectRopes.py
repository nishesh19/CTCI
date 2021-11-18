from heapq import heappush, heappop


def minimum_cost_to_connect_ropes(ropeLengths):
    result = []
    for rope in ropeLengths:
        heappush(result, rope)

    total_cost = [heappop(result) + heappop(result)]
    running_cost = total_cost[0]
    while result:
        curr_cost = heappop(result)

        if (not result) or running_cost < result[0]:
            running_cost += curr_cost
            total_cost.append(running_cost)
        else:
            next_cost = heappop(result)
            running_cost += curr_cost + next_cost
            total_cost.append(curr_cost+next_cost)
            total_cost.append(running_cost)
        #   heappush(result,curr_cost + next_cost)

    return sum(total_cost)


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
