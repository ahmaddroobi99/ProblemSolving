class Solution :
    def isOneBitCharacter(self, bits: List[int]) -> bool:
                length = len(bits)
                i = 0

                while i < length-1:
                    if bits[i] == 1:
                        i += 2
                    else:
                        i += 1

                i += 1

                return i == length