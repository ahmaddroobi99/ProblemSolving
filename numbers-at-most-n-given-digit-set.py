class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:

        abhi = defaultdict(int)
        for i in digits:
            abhi[int(i)] = 1

        def getlist(x):
            ans = []
            while x:
                ans.append(x % 10)
                x //= 10
            return ans[::-1]

        def getans(index, tight, prefix):
            if index == len(numlist):
                return 1

            if dp[index][tight][prefix] != -1 and tight != 1:
                return dp[index][tight][prefix]

            if tight:
                k = numlist[index]
            else:
                k = 9
            ret = 0

            for i in range(k + 1):
                newtight = 0

                if i == numlist[index]:
                    newtight = tight

                if abhi[i] == 1:
                    ret += getans(index + 1, newtight, 0)
                else:
                    if i == 0 and prefix:
                        ret += getans(index + 1, newtight, prefix)

            if not tight:
                dp[index][tight][prefix] = ret
            return ret

        numlist = getlist(n)
        print(numlist)
        dp = [[[-1 for i in range(2)] for j in range(2)] for k in range(20)]

        return getans(0, 1, 1) - 1