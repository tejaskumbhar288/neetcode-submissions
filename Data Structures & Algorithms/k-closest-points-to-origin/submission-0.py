import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for point in points:
            x1 = point[0]
            y1 = point[1]
            distance = math.sqrt(x1 * x1 + y1 * y1)

            heapq.heappush(heap, (distance, [x1, y1]))

        while k > 0:
            closest = heapq.heappop(heap)
            result.append(closest[1])
            k -= 1

        return result