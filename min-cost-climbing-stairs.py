class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1=cost[0]
        prev2=cost[1]
        for i in range(2,len(cost)):
            temp=cost[i]+min(prev1,prev2)
            prev1=prev2
            prev2=temp
        return min(prev2,prev1)