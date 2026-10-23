class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root

        for ch in word:
            if ch not in current.childrens:
                current.childrens[ch] = TrieNode()

            current = current.childrens[ch]

        current.is_end = True


    def search(self, word: str) -> bool:
        current = self.root

        for ch in word:
            if ch not in current.childrens:
                return False
            
            current = current.childrens[ch]

        return current.is_end
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for ch in prefix:
            if ch not in current.childrens:
                return False

            current = current.childrens[ch]

        return True
        
        