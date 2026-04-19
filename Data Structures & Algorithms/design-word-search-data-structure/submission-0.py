class WordDictionary:

    def __init__(self):
        self.trie={}
        
    def addWord(self, word: str) -> None:
        d=self.trie
        for c in word:
            if c not in d:
                d[c]={}
            d=d[c]
        d['*']='*'

    def search(self, word: str) -> bool:
        def dfs(i,node):
            if i==len(word):
                return '*' in node
            if word[i]=='.':
                for c in node:
                    if c!='*':
                        if dfs(i+1,node[c]):
                            return True
                return False
            else:
                if word[i] not in node:
                    return False
                return dfs(i+1, node[word[i]])
        return dfs(0,self.trie)
        

            
        

        
