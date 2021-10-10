class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_set = set()
        max_set = set()

        # Getting minimum element from each row
        for r in matrix:
            min_set.add(min(r))

        # Getting maximum element from each column
        for c in zip(*matrix):
            max_set.add(max(c))

        # Checking the common elements from both sets
        if min_set & max_set:
            return list(min_set & max_set)
        else:
            return []