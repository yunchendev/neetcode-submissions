class TrieNode:
    def __init__(self):
        self.children = {}

class SuffixTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, text: str):
        node = self.root
        for char in text:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

    def search(self, pattern: str):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len, reverse=True)

        trie = SuffixTrie()
        result = []

        for word in words:
            if trie.search(word):
                result.append(word)

            for i in range(len(word)):
                trie.insert(word[i:])

        return result

