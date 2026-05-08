class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)

        adj_list = defaultdict(list)
        # populate adj list
        for i in range(n - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            min_len = min(len(word_1), len(word_2))

            if len(word_1) > len(word_2) and word_1[:min_len] == word_2[:min_len]:
                return ""
                
            for j in range(min_len):
                char_1 = word_1[j]
                char_2 = word_2[j]

                if char_1 != char_2:
                    if char_2 not in adj_list[char_1]:
                        adj_list[char_1].append(char_2)
                    break
        
        print(adj_list)

        all_chars = set()

        for word in words:
            for char in word:
                all_chars.add(char)
        


        # build in degree map

        in_degree_map = Counter()
    
        for char in all_chars:
            for item in adj_list[char]:
                in_degree_map[item] += 1

        print(in_degree_map)

        queue = deque()

        for char in all_chars:
            if in_degree_map[char] == 0:
                queue.append(char)

        result = []

        while queue:
            curr_char = queue.popleft()
            result.append(curr_char)

            for neighbor in adj_list[curr_char]:
                in_degree_map[neighbor] -= 1

                if in_degree_map[neighbor] == 0:
                    queue.append(neighbor)

        return ''.join(result) if len(result) == len(all_chars) else ""
            