class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = -1
        my_dict = {}
        
        for num in arr:
            my_dict[num] = my_dict.get(num, 0) + 1

        for key in my_dict:
            if key == my_dict[key]:
                lucky = max(lucky, key)

        return lucky