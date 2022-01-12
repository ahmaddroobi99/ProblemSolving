class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                n1 = num[:i]
                n2 = num[i:j]

                if (n1[0] == '0' and i > 1) or (n2[0] == '0' and j - i > 1):
                    continue

                while j < n:
                    n3 = str(int(n1) + int(n2))
                    if not num.startswith(n3, j):
                        break

                    j += len(n3)
                    n1, n2 = n2, n3

                if j == n:
                    return True

        return False

