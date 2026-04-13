class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        phone={
            "2":"abc","3":"def","4":"ghi","5":"jkl",
            "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        res=[]

        def lettres(i,curr):
            if i==len(digits):
                res.append("".join(curr))
                return
            for l in phone[digits[i]]:
                curr.append(l)
                lettres(i+1,curr)
                curr.pop()
        lettres(0,[])
        return res