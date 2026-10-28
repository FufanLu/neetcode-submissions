class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        return self._dfs(self.root, word, 0)

    def _dfs(self, node, word, i):
        curr = node
        while i < len(word) and word[i] != '.':
            s = word[i]
            if s not in curr.children:
                return False
            curr = curr.children[s]
            i += 1

        if i == len(word):
            return curr.isEnd

        for child in curr.children.values():
            if self._dfs(child, word, i + 1):
                return True

        return False

        
                
            
        
        
