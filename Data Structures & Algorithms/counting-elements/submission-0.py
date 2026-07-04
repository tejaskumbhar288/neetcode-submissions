class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0

        for i in range(len(arr)):
            temp = arr[i] + 1
            if temp in arr:
                count += 1

        return count