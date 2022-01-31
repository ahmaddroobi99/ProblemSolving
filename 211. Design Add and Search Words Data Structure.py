class Trie:
    def __init__(self):
        self.wordend = False
        self.alpha = {}


class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def insertTrie(self, root, word):
        if not word:
            root.wordend = True
            return root
        w = word[0]
        if w not in root.alpha:
            root.alpha[w] = Trie()
        root.alpha[w] = self.insertTrie(root.alpha[w], word[1:])
        return root

    def matchWord(self, root, word) -> bool:
        if not word:
            return root.wordend
        if not root:
            return False
        w = word[0]
        if w in root.alpha:
            return self.matchWord(root.alpha[w], word[1:])
        elif w == ".":
            for alphabet in root.alpha:
                if self.matchWord(root.alpha[alphabet], word[1:]):
                    return True
        return False

    def addWord(self, word: str) -> None:
        self.root = self.insertTrie(self.root, word)

    def search(self, word: str) -> bool:
        return self.matchWord(self.root, word)