class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        n = len(nums)
        self.prefix_sum = [0] * n
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            self.prefix_sum[i] = total

        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]

        return (self.prefix_sum[right] - self.prefix_sum[left-1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)