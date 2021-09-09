class Trie:
    def __init__(self):
        self.child = {}
        self.cnt = 0

    def insert(self, string):
        curr = self
        for char in string:
            curr.cnt += 1
            if char not in curr.child:
                curr.child[char] = Trie()
            curr = curr.child[char]
        curr.cnt += 1

    def search(self, string):
        curr = self
        for char in string:
            if char == '?':
                return curr.cnt
            if char not in curr.child:
                return 0
            curr = curr.child[char]
        return curr.cnt


def solution(words, queries):
    TrieRoot = [Trie() for _ in range(10000)]
    ReTrieRoot = [Trie() for _ in range(10000)]
    answer = []

    for string in words:
        TrieRoot[len(string) - 1].insert(string)
        ReTrieRoot[len(string) - 1].insert(string[::-1])

    for string in queries:
        if string[0] != '?':
            answer.append(TrieRoot[len(string) - 1].search(string))
        else:
            answer.append(ReTrieRoot[len(string) - 1].search(string[::-1]))

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = [3, 2, 4, 1, 0]
print(solution(words, queries))
