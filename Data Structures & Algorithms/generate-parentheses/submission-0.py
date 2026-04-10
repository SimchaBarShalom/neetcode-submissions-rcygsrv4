class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def generateparenthesis(left,right,generate):
            if left==0 and right==0:
                res.append(generate)
                return 
            if left>0:
                generateparenthesis(left-1,right,generate+"(")
            if right>left:
                generateparenthesis(left,right-1,generate+")")
        generateparenthesis(n,n,"")
        return res

            