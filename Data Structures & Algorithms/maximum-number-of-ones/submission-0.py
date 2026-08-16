class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        counts = []
        for i in range(sideLength):
            for j in range(sideLength):
                # number of times offset (i, j) appears
                cnt = ((height - 1 - i) // sideLength + 1) * ((width - 1 - j) // sideLength + 1)
                counts.append(cnt)
        
        counts.sort(reverse=True)
        return sum(counts[:maxOnes])