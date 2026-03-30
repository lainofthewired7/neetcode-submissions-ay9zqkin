class WordDictionary:

    def __init__(self):

        self.children = {}

        self.isWord = False

        
        
    def addWord(self, word: str) -> None:

        curr = self

        for char in word:

            if char not in curr.children:

                curr.children[char] = WordDictionary()

            curr = curr.children[char]

        curr.isWord = True
        

    def search(self, word: str) -> bool:

        curr = self

        for i in range (len(word)):

            if word[i] not in curr.children and word[i] != ".":

                return False

            if not curr.children:

                return False

            if word[i] == ".":

                valid = False

                for char in curr.children:

                    valid = valid or curr.children[char].search(word[i+1:])

                return valid

            curr = curr.children[word[i]]

        return curr.isWord
        
