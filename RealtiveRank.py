
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hashmap = {}
        s = sorted(score)[::-1]
        for i in range(len(score)):
            if i == 0:
                hashmap[s[i]] = "Gold Medal"
            elif i == 1:
                hashmap[s[i]] = "Silver Medal"
            elif i == 2:
                hashmap[s[i]] = "Bronze Medal"
            else:
                hashmap[s[i]] = str(i+1)
        return [hashmap[i] for i in score]