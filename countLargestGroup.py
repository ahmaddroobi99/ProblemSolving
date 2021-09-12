class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Function to get sum of digits
        def get_sum(value):
            res = 0

            while value:
                res += (value % 10)
                value //= 10

            return res

        # Dictionary to group values with same sum eg - [1,10] having sum 1
        # So, in d it will be stored as {1:2},i,e, 1 occuring 2 times as sum
        d = {}

        # Looping & storing values in d
        for i in range(1, n + 1):
            temp = get_sum(i)
            if temp not in d:
                d[temp] = 1
            else:
                d[temp] += 1

        # Finding the maximum size of group
        maxSize = max(d.values())
        ans = 0

        # Finding how many groups are there with maxSize groups
        for i in d:
            if d[i] == maxSize:
                ans += 1
        # Returning ans
        return ans