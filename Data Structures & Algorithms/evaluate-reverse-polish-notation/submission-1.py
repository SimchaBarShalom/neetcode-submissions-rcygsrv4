class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in  range (len(tokens)):
            if tokens[i] in ['+','-','*','/']:
                n1=s.pop()
                n2=s.pop()
                if tokens[i]=='+':
                    nums=n1+n2
                elif tokens[i]=='-':
                    nums=n2-n1
                elif tokens[i]=='*':
                    nums=n1*n2
                elif tokens[i]=='/':
                    nums=int(n2/n1)
                s.append(nums)
            else:
                s.append(int(tokens[i]))
        return s[0]

        
                
                


        