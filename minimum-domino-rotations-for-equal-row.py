class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if len(tops) <= 1:
            return 0

        def helper(target, tops, bottoms):
            count = 0

            for i in range(len(tops)):
                t, b = tops[i], bottoms[i]
                if target == t:
                    continue

                else:
                    if target == b:
                        count += 1

                    else:
                        count = float("inf")
                        break

            return count

        res = min(helper(tops[0], tops, bottoms), helper(tops[0], bottoms, tops), helper(bottoms[0], tops, bottoms),
                  helper(bottoms[0], bottoms, tops))

        return res if res != float("inf") else -1
