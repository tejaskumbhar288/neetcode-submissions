class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isPossible(mid:int, weights: List[int], days: int) -> bool:
            total_days = 1
            total_sum = 0

            for weight in weights:
                if total_sum + weight <= mid:
                    total_sum += weight
                else:
                    total_sum = weight
                    total_days += 1

            return total_days <= days

        
        
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = low + (high - low) // 2

            if isPossible(mid, weights, days):
                high = mid
            
            else:
                low = mid + 1


        return low