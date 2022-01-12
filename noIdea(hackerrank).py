a = input().split(' ')
l = ([int(i) for i in input().split(' ')])
firstset = {int(i) for i in input().split(' ')}
secondset = {int(i) for i in input().split(' ')}
p = 0
for i in l:
    if i in firstset:
        p += 1
    if i in secondset:
        p -= 1
print(p)
