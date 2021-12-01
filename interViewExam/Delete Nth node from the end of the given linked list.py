
class LisnkedList:
    def __init__(self,data, next):
        data = self.data
        next =self.next



# complexity simply O(3*N)==O(N)
class Solution :
    def Delete_N_Position (  headList ,N) :
        p= headList
        count= 0
        while (p):
            count+=1
            p=p.next
        traget =count -N
        p2 =headList
        while(traget>0):
            p=p.next
            traget-=1

        while(True) :
            if p2.next==p :
                break  # by now i have p in the node i wanna delete and the p2 in the previous node

        p2.next =p.next
        return headList







