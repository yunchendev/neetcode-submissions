class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        queue = deque([(beginWord, 1)])

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for char in 'qwertyuiopasdfghjklzxcvbnm':
                    new_word = word[:i] + char + word[i + 1:]

                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, length + 1))

        return 0