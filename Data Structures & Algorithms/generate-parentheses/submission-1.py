class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def parenthesis(left,right,generate):
            if left==0 and right==0:
                res.append(generate)
                return 
            if left>0:
                parenthesis(left-1,right,generate+"(")
            if right>left:
                parenthesis(left,right-1,generate+")")
        parenthesis(n,n,"")
        return res

            