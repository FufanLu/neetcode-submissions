class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0


        patterns = defaultdict(list)
        
        for w in wordList + [beginWord]:
            for i in range(len(w)):
                patterns[w[:i] + '*' + w[i + 1 :]].append(w)

        
        visited = set()
        visited.add(beginWord)

        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1 :]
                for child in patterns[key]:
                    if child not in visited:
                        visited.add(child)
                        queue.append((child, step + 1))

        return 0  







