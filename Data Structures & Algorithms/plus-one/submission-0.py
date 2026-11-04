class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits)-1, -1, -1):
            total = digits[i] + carry
            carry = 0

            if total >= 10:
                carry = 1
                total = total % 10
                digits[i] = total

                if i == 0:
                    digits.insert(0, carry)

            else:
                digits[i] = total
                break

        return digits