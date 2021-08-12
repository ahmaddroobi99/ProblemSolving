class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):

        # Find the dimensions of the given rectangles
        w1 = abs(C - A)
        h1 = abs(D - B)
        w2 = abs(G - E)
        h2 = abs(H - F)

        # Compute the sum of the areas of both rectangles
        area = w1 * h1 + w2 * h2

        if (G < A) or (E > C) or (F > D) or (H < B):  # Conditions for no overlap (if G is left of A, etc.)
            return area
        else:
            I = max(A, E)  # Leftmost x position will be the rightmost of the two left x positions
            J = max(B, F)  # Lower y position will be the higher of the two lower y positions
            K = min(C, G)  # Rightmost y position will be the leftmost of the two right x positions
            L = min(D, H)  # Higher y position will be the lower of the two higher y positions

            # Find dimensions of overlapping section
            w3 = abs(K - I)
            h3 = abs(L - J)

            # Return the summed area minus the area of the overlapping section
            return area - (w3 * h3)