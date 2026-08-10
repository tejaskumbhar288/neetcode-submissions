# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # Start the recursive process on the full array
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
    
    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        # Base case: if the subarray has 0 or 1 elements, it's already sorted
        if e - s + 1 <= 1:
            return pairs
        
        # Find the middle point
        m = (s + e) // 2
        
        # Recursively sort left and right halves
        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)
        
        # Merge the sorted halves
        self.merge(pairs, s, m, e)
        
        return pairs
    
    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> None:
        # Copy both halves to temporary arrays
        L = arr[s:m + 1]  # Left half: indices s to m
        R = arr[m + 1:e + 1]  # Right half: indices m+1 to e
        
        # Merge pointers
        i = 0  # index for L
        j = 0  # index for R
        k = s  # index for original array
        
        # Compare and merge
        while i < len(L) and j < len(R):
            # Use <= for stability - when equal, take from left first
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Copy remaining elements from L (if any)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        # Copy remaining elements from R (if any)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
