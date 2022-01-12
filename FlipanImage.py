class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        newImage = []
        for row in image:
            new_row = [1 ^ x for x in row[::-1]]
            newImage.append(new_row)

        return newImage