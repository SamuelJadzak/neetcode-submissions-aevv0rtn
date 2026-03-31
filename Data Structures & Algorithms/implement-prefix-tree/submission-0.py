class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curnode = self.root
        for ch in word:
            if ch in curnode.children.keys():
                curnode = curnode.children[ch]
            else:
                curnode.children.update({ch : TrieNode()})
                curnode = curnode.children[ch]
        curnode.isEndOfWord = True

    def search(self, word: str) -> bool:
        curnode = self.root
        for ch in word:
            if ch in curnode.children.keys():
                curnode = curnode.children[ch]
            else:
                return False
        return curnode.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curnode = self.root
        for ch in prefix:
            if ch in curnode.children.keys():
                curnode = curnode.children[ch]
            else:
                return False
        return True
        
        