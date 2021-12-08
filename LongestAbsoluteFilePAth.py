
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines =input.split("\n")
        maxLength = 0
        depth_map = {0: 0}
        for line in lines:
            path = line.split("\t")[-1]
            depth = len(line) - len(path)

            if '.' in path:
                maxLength = max(maxLength, depth_map[depth] + len(path))
            else:
                depth_map[depth + 1] = depth_map[depth] + len(path) + 1

        return maxLength
