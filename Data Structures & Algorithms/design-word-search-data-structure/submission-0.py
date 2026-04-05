class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        return self.dfs(0, self.root, word)
            
    def dfs(self, index, node, word):
        if index == len(word):
            return node.endOfWord

        char = word[index]

        if char == '.':
            for child in node.children.values():
                if self.dfs(index + 1, child, word):
                    return True
            return False

        else:
            if char not in node.children:
                return False
            return self.dfs(index + 1, node.children[char], word)
