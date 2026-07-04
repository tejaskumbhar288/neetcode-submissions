class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        my_dict = {}

        for i in range(len(keyboard)):
            my_dict[keyboard[i]] = i

        leftCount = 0
        sum = 0
        for i in range(len(word)):
            tempSum = abs(my_dict[word[i]] - leftCount)
            leftCount = my_dict[word[i]]
            sum += tempSum

        return sum
