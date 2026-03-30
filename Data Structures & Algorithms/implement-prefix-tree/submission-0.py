class PrefixTree:

    def __init__(self):

        self.mapping = {}

        self.isComplete = False
        

    def insert(self, word: str) -> None:

        curr = self

        for i in range (len(word)):

            if word[i] not in curr.mapping:

                newNode = PrefixTree()

                curr.mapping[word[i]] = newNode
            
            curr = curr.mapping[word[i]]

        curr.isComplete = True
                

    def search(self, word: str) -> bool:

        curr = self

        for char in word:

            if char not in curr.mapping:

                return False

            curr = curr.mapping[char]

        return curr.isComplete


    def startsWith(self, prefix: str) -> bool:

        curr = self

        for char in prefix:

            if char not in curr.mapping:

                return False

            curr = curr.mapping[char]

        return True

        
        