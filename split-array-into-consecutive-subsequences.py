
from collections import Counter
class Solution(object):

    def isPossible(self, nums):
        count = Counter(nums)
        tails = Counter()
        for x in nums:
            if count[x] == 0:
                continue
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x+1] += 1
            elif count[x+1] > 0 and count[x+2] > 0:
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                return False
            count[x] -= 1
        return True