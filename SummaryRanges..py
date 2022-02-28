class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        start, cur, end = nums[0], nums[0], None
        output = []

        for n in nums[1:]:
            cur += 1
            if n == cur:
                end = n
            else:
                if not end:
                    output.append(str(start))
                else:
                    output.append(str(start) + "->" + str(end))
                start = n
                cur = n
                end = None
        if not end:
            output.append(str(start))
        else:
            output.append(str(start) + "->" + str(end))

        return output



