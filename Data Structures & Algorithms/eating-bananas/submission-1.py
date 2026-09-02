import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(mid:int, piles:List[int], h:int) -> bool:
            total = 0

            for pile in piles:
                total += math.ceil(pile / mid)

            return total <= h
        
        
        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high - low)//2

            if isPossible(mid, piles, h):
                high = mid
            else:
                low = mid + 1

        return low