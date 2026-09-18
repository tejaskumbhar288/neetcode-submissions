import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x, y = point
            distance = x * x + y * y

            # Max heap using negative distance
            heapq.heappush(heap, (-distance, point))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _, point in heap]