class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        mapping = {0: 0, 1: 0}
        for prefer in students:
            mapping[prefer] = mapping.get(prefer, 0) + 1


        for sandwhich in sandwiches:
            if mapping.get(sandwhich, 0) != 0:
                mapping[sandwhich] -= 1

            else:
                break

        return sum(mapping.values())