class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        [A,B,C,D], [E,F,G,H] = rec1, rec2
        return F<D and E<C and B<H and A<G