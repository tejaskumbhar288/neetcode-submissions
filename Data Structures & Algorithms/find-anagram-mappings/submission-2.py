class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict = {}
        result = [0] * len(nums1)

        for index, num in enumerate(nums2):
            my_dict[num] = index

        for i, num in enumerate(nums1):
            result[i] = my_dict[num]

        return result
