class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force
        # Time Complexity: O(N^2)
        # Space Complexity: O(1)

        #         NetProfit=0
        #         for i in range (len(prices)):
        #             for j in range (i+1,len(prices),1):
        #                 TemppProfit=prices[j]-prices[i]
        #                 if (NetProfit<TemppProfit):
        #                     NetProfit=TemppProfit
        #         return (NetProfit)
        # 2. Optimized Solution

        #  #Optimized Solution:
        #         #Time Complexity: O(N)
        #         #Space Complexity: O(1)

        NetProfit = 0
        MinimumPrice = prices[0]
        for i in range(len(prices)):
            if (MinimumPrice > prices[i]):
                MinimumPrice = prices[i]
            Tempprofit = prices[i] - MinimumPrice
            if (Tempprofit > NetProfit):
                NetProfit = Tempprofit
        return (NetProfit)
# COMPLEXITIES:

#  1. Brute force Solution
#         Time Complexity: O(N^2)
#         Space Complexity: O(1)

# ----------------------------------------------

#  2. Optimized Solution:
#         Time Complexity: O(N)
#         Space Complexity: O(1)