class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        my_map = [0] * len(words)
        vowel = "aeiou"
        vowel_count = 0
        result = [0] * len(queries)

        for i in range(len(words)):
            word = words[i]
            my_map[i] = vowel_count

            if len(word) == 1 and word[0] in vowel:
                vowel_count += 1
            if len(word) > 1:
                if word[0] in vowel and word[len(word)-1] in vowel:
                    vowel_count += 1

            my_map[i] = vowel_count

        print("My map = ", my_map)
        for i in range(len(queries)):
            first = queries[i][0]
            second = queries[i][1]

            if first == 0:
                result[i] = my_map[second]
            else:
                result[i] = my_map[second] - my_map[first - 1]

            
        return result