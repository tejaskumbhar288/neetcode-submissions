from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):
            # 1. Remove indices outside the window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2. Remove smaller elements
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Once window reaches size k, record maximum
            if i >= k-1:
                result.append(nums[dq[0]])

        return result