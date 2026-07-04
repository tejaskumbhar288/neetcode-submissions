class Solution:
    def stringShift(self, s: str, shifts: List[List[int]]) -> str:
        leftShift = 0
        rightShift = 0

        for shift in shifts:
            if shift[0] == 0:
                leftShift += shift[1]
            else:
                rightShift += shift[1]

        total = leftShift - rightShift

        leftShift = total % len(s)

        result = s[leftShift:] + s[:leftShift]

        return result