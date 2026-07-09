class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Brute force solution
        len2 = len(nums2)
        nextGreater = [-1] * len2
        mapping = {}

        for i in range(len(nums2)):
            mapping[nums2[i]] = i
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    nextGreater[i] =  (nums2[j])
                    break

        result = []
        for i in range(len(nums1)):
            index = mapping[nums1[i]]
            result.append(nextGreater[index])

        return result