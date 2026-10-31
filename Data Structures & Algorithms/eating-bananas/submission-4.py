class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(mid: int):
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)

            return hours <= h

        
        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high - low) // 2

            if isPossible(mid):
                high = mid

            else:
                low = mid + 1

        return low