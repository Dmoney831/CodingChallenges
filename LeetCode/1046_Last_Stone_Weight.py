import heapq
def lastStoneWeight(stones):
    stack = stones
    stack.sort()
    # heapq.heapify(stones)
    while len(stack) >= 2:
        x, y = stack[-2], stack[-1]
        z = y - x
        if z > 0:
            stack.pop()
            stack[-1] = z
            stack.sort()
        if z == 0:
            stack.pop()
            stack.pop()
    return len(stack)

stones = [1]
stones = [2,7,4,1,8,1]
# stones = [1,3]
# ***********optimal solution**********
def lastStoneWeight(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)
    # print(stones)
    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        # print(first, second)
        if second > first:
            heapq.heappush(stones, first - second)
    stones.append(0)
    return abs(stones[0])

print(lastStoneWeight(stones))
# *********Time Complexity: O(nlogn)