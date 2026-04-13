class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        curr=[]
        n=len(s)
        dp=[[False]*(n+1) for i in range(n+1)]      
        for end in range(n):
            for start in range(end,-1,-1):
                if s[start]==s[end] and (end-start<=2 or dp[start+1][end-1]):
                    dp[start][end] = True

        def subPalindrome(i):
            if i>=n:
                res.append(curr.copy())
                return 
            for j in range(i, n):
                if dp[i][j]:
                    curr.append(s[i:j+1])
                    subPalindrome(j + 1)
                    curr.pop()
        subPalindrome(0)
        return res