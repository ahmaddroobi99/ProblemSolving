class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        out = []
        for i in nums:
            while True:
                i = i // 10
                count += 1
                if i == 0:
                    out.append(count)
                    count = 0
                    break
        even = 0
        for i in out:
            if i % 2 == 0:
                even += 1

        return even

