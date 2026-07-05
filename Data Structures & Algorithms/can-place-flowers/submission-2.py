class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def checkAdjacent(self, flowerbed: List[int], i:int) -> bool:
            if (i-1) >= 0 and flowerbed[i-1] == 1:
                return False
            if (i + 1) < len(flowerbed) and flowerbed[i+1] == 1:
                return False

            return True

        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] != 1 and checkAdjacent(self, flowerbed, i):
                flowerbed[i] = 1
                count += 1

        return count >= n