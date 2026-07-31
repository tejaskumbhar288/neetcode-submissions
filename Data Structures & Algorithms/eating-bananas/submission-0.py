class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isCorrect(mid:int, piles: List[int], h:int) -> bool:
            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid -1) // mid
                #or total_hours += ceil(pile / mid)

            return total_hours <= h
        
        
        low = 1
        high = max(piles)
        result = -1

        while low <= high:
            mid = (low + high) //2

            if isCorrect(mid, piles, h):
                result = mid
                high = mid - 1

            else:
                low = mid + 1

        return result