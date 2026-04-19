class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            d=trie
            for c in word:
                if c not in d:
                    d[c]={}
                d=d[c]
            d['.']='.'
        rows,cols=len(board),len(board[0])
        res=set()

        def dfs(r,c,node,current_word):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]=='#' or board[r][c] not in node:
                return 
            char=board[r][c]
            word_node=node[char]
            current_word+=char
            if '.' in word_node:
                res.add(current_word)
            board[r][c]='#'
            dfs(r+1,c,word_node,current_word)
            dfs(r-1,c,word_node,current_word)
            dfs(r,c+1,word_node,current_word)
            dfs(r,c-1,word_node,current_word)
            board[r][c]=char
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,trie,"")
        return list(res)