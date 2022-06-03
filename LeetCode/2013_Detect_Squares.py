from collections import defaultdict
from collections import Counter

class DetectSquares:

    def __init__(self):
        self.ptsCounts = Counter()

    def add(self, point: List[int]) -> None:
        self.ptsCounts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point
        for (x3, y3), pts in self.ptsCounts.items():
            if abs(x1 - x3) == 0 or abs(x1 - x3) != abs(y1- y3):
                continue
            ans += pts * self.ptsCounts[(x1, y3)] * self.ptsCounts[(x3, y1)]
        return ans