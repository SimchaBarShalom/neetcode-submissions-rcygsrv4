class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def checkWord(i,j,k):
            if k==len(word):
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[k]:
                return False
            if board[i][j]==word[k]:
                temp=board[i][j]
                board[i][j]=" " 
                check=  (checkWord(i+1,j,k+1) or
                         checkWord(i-1,j,k+1) or
                         checkWord(i,j+1,k+1) or
                         checkWord(i,j-1,k+1))
                board[i][j]=temp
                if check:
                    return True
            return False
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(checkWord(i,j,0)):
                    return True
        return False
        