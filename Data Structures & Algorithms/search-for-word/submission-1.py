class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def checkWord(i,j,k):
            if k==len(word):
                return True
            if k==0 and j==len(board[0]):
                return checkWord(i+1,0,0)
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False
            if board[i][j]==word[k]:
                temp=board[i][j]
                board[i][j]=" " 
                check= (checkWord(i+1,j,k+1) or
                         checkWord(i-1,j,k+1) or
                         checkWord(i,j+1,k+1) or
                         checkWord(i,j-1,k+1))
                board[i][j]=temp
                if check:
                    return True
            if k==0:
                return checkWord(i,j+1,0)
            return False
        return checkWord(0,0,0)