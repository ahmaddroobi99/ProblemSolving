hashmap = {}

for i in s:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

for i in t:
    if i in hashmap:
        hashmap[i] -= 1
        if hashmap[i] == 0:
            hashmap.pop(i)

    else:
        return i
return hashmap.item[0]