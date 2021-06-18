a=input().split(' ')
l=([int(i) for i in input().split(' ')])
firstset=set([int(i) for i in input().split(' ')])
secondset=set([int(i) for i in input().split(' ')])
p=0
for i in l:
    if i in firstset:
        p+=1
    if i in secondset:
        p-=1
print(p)