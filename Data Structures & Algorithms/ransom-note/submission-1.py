class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_dict = {}
        for ch in magazine:
            my_dict[ch] = my_dict.get(ch, 0) + 1

        for ch in ransomNote:
            if ch not in my_dict:
                return False

            my_dict[ch] -= 1
            if my_dict[ch] == 0:
                del my_dict[ch]

        return True