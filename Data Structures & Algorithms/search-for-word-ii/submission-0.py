class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ''

class Solution:
    def addWord(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()

        for word in words:
            self.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res = set()

        def dfs(r, c, node):
            char = board[r][c]

            # get the child node

            child_node = node.children[char]

            # check if we found a word
            if child_node.word:
                res.add(child_node.word)
                child_node.word = ''

            # mark visited

            board[r][c] = '#'

            # explore neighbors

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in child_node.children):
                    dfs(nr, nc, child_node)
            
            # backtrack

            board[r][c] = char

        # start dfs from every cell if that's the start of a word

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in self.root.children:
                    dfs(r, c, self.root)

        
        return list(res)



    