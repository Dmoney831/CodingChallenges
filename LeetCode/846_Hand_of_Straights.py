from collections import Counter
def isNStraightHand(hand, groupSize):
    c = Counter(hand)
    for i in sorted(c):
        if c[i] > 0:
            for j in range(groupSize)[::-1]:
                print(i, j, c[i+j])
                c[i + j] -= c[i]
                if c[i + j] < 0:
                    return False
    return True
        
# ******Time Complexity: O(nlogn + n*groupSize) where n is the number of different cards.
import heapq
def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize:
        return False
    
    count = {}
    for n in hand:
        count[n] = 1 + count.get(n, 0)
    
    minH = list(count.keys())
    heapq.heapify(minH)
    while minH:
        first = minH[0]
        for i in range(first, first + groupSize):
            if i not in count:
                return False
            count[i] -= 1
            if count[i] == 0:
                if i != minH[0]:
                    return False
    return True

# ******Time Complexity: O(n*logn)

    
# hand = [1,2,3,3,5,6,7,8,9]
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
# Output: true

# hand = [1,2,3,4,5]
# groupSize = 4
# Output: false
print(isNStraightHand(hand, groupSize))


