class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        my_dict = {}

        for ch in arr:
            my_dict[ch] = my_dict.get(ch, 0) + 1

        print("My_dict = ", my_dict)


        i = 1
        for key in my_dict:
            if i == k and my_dict[key] == 1:
                return key
            
            if my_dict[key] == 1:
                i += 1        

        return ""