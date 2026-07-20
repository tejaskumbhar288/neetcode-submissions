class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ""
        for i in range(len(num) - 2):
            temp = num[i:i+3]
            if temp[0] == temp[1] == temp[2]:
                largest = max(largest, temp)

            
        return largest
