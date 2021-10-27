class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        '''
        Take s = "dcab", pairs = [[0,3],[1,2]] as example.

        1. At first we create UnionFind structure.
        2. Next step is filling it with pairs. Here let's
            look more precisely: self.root = [0,1,2,3] at first,
            then we merge 0&3 and 1&2 => self.root = [0,1,1,0],
            so we're uniting some roots.

        3. Create 2 dict: first to keep letters and second to keep idx.
        4. Traverse input string.
        5. Look for # in code to get how dict1 and dict2 look like.
        6. We sort them to get lexicographically smallest first
        7. Next we take key, 0 at first, and as we have `key: list`
            => we can pick up letter based on idx as well. As letters
            are sorted in smallest to biggest order => we take smallest first
            and put it into position that is written in dict2 (it is from smallest
            to biggest without sort)

        8. At first we fill: ['b', _, _, 'd'] and next we fill with 1 key.

        '''
        graph = UnionFind(len(s))

        for pair in pairs:
            graph.union(pair[0], pair[1])

        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            root = graph.find(i)
            if root not in dict1:
                dict1[root] = []

            if root not in dict2:
                dict2[root] = []

            dict1[root].append(s[i])
            dict2[root].append(i)

        result = [0 for _ in range(len(s))]
        # dict1: {0: ['d', 'b'], 1: ['c', 'a']}
        # dict2: {0: [0, 3], 1: [1, 2]}
        for k in dict1:
            dict1[k].sort()
            # we sort to get lexicographically
            # smallest letters first
            for i in range(len(dict2[k])):
                result[dict2[k][i]] = dict1[k][i]

        return "".join(result)


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.count = size

    def find(self, vert):
        if self.root[vert] == vert:
            return vert
        self.root[vert] = self.find(self.root[vert])
        return self.root[vert]

    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            if self.rank[r1] > self.rank[r2]:
                self.root[r2] = r1
            elif self.rank[r1] < self.rank[r2]:
                self.root[r1] = r2
            else:
                self.root[r2] = r1
                self.rank[r1] += 1

            self.count -= 1