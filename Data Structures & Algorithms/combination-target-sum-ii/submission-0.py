class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):

                # Skip duplicate choices at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since the array is sorted,
                # nothing after this can work
                if candidates[i] > remaining:
                    break

                #choose
                path.append(candidates[i])

                # Explore
                # i + 1 because each element can be used once
                backtrack(i+1, remaining - candidates[i])

                path.pop()

        backtrack(0, target)

        return result