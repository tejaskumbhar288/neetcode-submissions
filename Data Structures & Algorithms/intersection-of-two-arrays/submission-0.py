class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_set1 = set()
        my_set2 = set()
        result = []

        for num in nums1:
            my_set1.add(num)

        for num in nums2:
            my_set2.add(num)

        intersection = my_set1 & my_set2
        for num in intersection:
            result.append(num)

        return result
        