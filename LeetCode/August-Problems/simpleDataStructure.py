class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = collections.defaultdict(list)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if len(word) != 0:
            self.trie[len(word)].append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return False
        if '.' not in word:
            return True if word in self.trie[len(word)] else False
        
        for i in self.trie[len(word)]:
            for key, char in enumerate(word):
                if char != '.' and char != i[key]:
                    break
            else:
                return True
        return False
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)