class Solution:
    def numDecodings(self, s: str) -> int:

        m = {"1": 'A', "2": 'B', "3": 'C', "4": 'D', "5": 'E', "6": 'F', "7": 'G', "8": 'H', "9": 'I', "10": 'J',
             "11": 'K', "12": "L", "13": "M", "14": 'N', "15": 'O', "16": 'P', "17": 'Q', "18": 'R', "19": 'S',
             "20": 'T', "21": 'U', "22": 'V', "23": 'W', "24": 'X', "25": 'Y', "26": 'Z'}

        ## The dynamic programming approach to this problem would be analogous the fibonnaci series
        dp = [0 for _ in range(len(s) + 1)]
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):

            if s[i] in m:
                if i == len(s) - 1:
                    dp[i] = 1
                else:
                    dp[i] = dp[i] + dp[i + 1]
            if i + 1 < len(s) and s[i:i + 2] in m:
                # print(s[i:i+2])
                dp[i] = dp[i] + dp[i + 2]
        # print(dp)
        return dp[0]