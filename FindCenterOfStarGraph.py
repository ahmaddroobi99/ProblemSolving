class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        freq_dict = defaultdict(int)
        for edge in edges:
            for num in edge:
                freq_dict[num] += 1

        for num in freq_dict:
            if freq_dict[num] == len(edges):
                return num

        return False