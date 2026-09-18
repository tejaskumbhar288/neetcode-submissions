import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to negative values to simulate a max heap
        stones = [-stone for stone in stones]

        # Build the heap
        heapq.heapify(stones)

        while len(stones) > 1:
            # Get two heaviest stones
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            # If they are different, push their difference
            if x != y:
                heapq.heappush(stones, -(y - x))

        # Return the remaining stone, or 0
        return -stones[0] if stones else 0