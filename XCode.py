def getCount(rows, columns, A):
    res = 0

    for i in range(rows):
        for j in range(i + 1, rows, 1):
            if (A[i][0] * A[j][1] ==
                    A[i][1] * A[j][0]):
                res += 1

    return res


# Input
matrix = []
a = []

R = int(input())
print(R)
for i in range(R):

    for j in range(2):
        a.append(input().split())
        print(a)

    matrix.append(a)

print(getCount(R, 2, matrix))