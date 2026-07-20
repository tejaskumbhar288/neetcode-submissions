class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_dict = {}
        for ch in magazine:
            my_dict[ch] = my_dict.get(ch, 0) + 1

        for ch in ransomNote:
            if ransomNote.count(ch) > my_dict.get(ch, 0):
                return False

        return True