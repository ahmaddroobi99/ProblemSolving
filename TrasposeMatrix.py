class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
            hp = {}
            for i, r in enumerate(A):
                hp[i] = r

            output=[]
            for j in range(len(A[0])):
                tmp = [hp[i][j] for i in hp.keys()]
                output.append(tmp)
            return output