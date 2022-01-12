# class Solution:
#     def minSwaps(self, grid: List[List[int]]) -> int:
#         ans =0
#         n= len (grid)
#         tz =[]

#         for row in grid :
#             count =0
#             for i in range (n-1,-1,-1) :
#                 if row[i]==0 :
#                     count+=1
#                 else :
#                     break
#             tz.append(count)

#         for i ,count in enumerate(tz):
#             target = n-i-1

#             k=i
#             while k <n and tz[k]<target :
#                 k+=1

#                 if k==n :
#                     return -1

#                 ans+=k-i

#                 while k>i :
#                     tz[k],tz[k-1] =tz[k-1],tz[k]
#                     k-=1
#         return ans


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        lenth = len(grid)
        zeros = [0] * lenth
        for i in range(lenth):
            row = grid[i]
            for j in range(lenth):
                if row[-j - 1] == 0:
                    zeros[i] = j + 1
                else:
                    break

        count = 0

        for i in range(lenth):
            print(zeros)
            if zeros[i] < lenth - 1 - i:

                did = 0
                for next in range(lenth - i - 1):
                    if zeros[i + next + 1] >= lenth - 1 - i:
                        did = 1
                        k = i + next + 1
                        while k - i > 0:
                            count += 1
                            zeros[k], zeros[k - 1] = zeros[k - 1], zeros[k]
                            k -= 1
                        break

                if did == 0:
                    return -1
        return count
