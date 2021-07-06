class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dct = {}
        result = []
        for n in nums:
            if dct.get(n, 0):
                # find duplicate and quit from loop
                result.append(n)
                break
            else:
                dct[n] = 1
                # sum_of_correct_list - (nums_sum - duplicate) = missing_number
        result.append(sum(range(1, len(nums)+1)) - (sum(nums) - result[0]))
        return result
