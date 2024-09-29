class Trie:

    def __init__(self):
        self.store = {}

    def insert(self, word: str) -> None:
        self.store[word] = self.store.get(word, 0) + 1

    def countWordsEqualTo(self, word: str) -> int:
        return self.store.get(word, 0)

    def countWordsStartingWith(self, prefix: str) -> int:
        count = 0
        for key, value in self.store.items():
            if prefix == key[0:len(prefix)]:
                count += value
        return count

    def erase(self, word: str) -> None:
        if word in self.store:
            self.store[word] -= 1
            if self.store[word] == 0:
                del self.store[word]


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)