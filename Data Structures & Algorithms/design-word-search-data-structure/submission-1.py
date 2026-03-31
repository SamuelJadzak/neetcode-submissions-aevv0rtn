class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curnode = self.root
        for ch in word:
            if ch not in curnode.children.keys():
                curnode.children.update({ch : TrieNode()})
            curnode = curnode.children[ch]
        curnode.isEndOfWord = True

    def search(self, word: str, curnode=None) -> bool:
        if curnode is None:
            curnode = self.root
        for i in range(len(word)):
            if word[i] == ".":
                goodWord = False
                for key in curnode.children.keys():
                    goodWord = goodWord or self.search(word[i+1:], curnode.children[key])
                return goodWord
            if word[i] not in curnode.children.keys():
                return False
            curnode = curnode.children[word[i]]
            
        return curnode.isEndOfWord
            
        


