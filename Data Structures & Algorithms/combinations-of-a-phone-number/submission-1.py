class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        phone={
            "2":"abc","3":"def","4":"ghi","5":"jkl",
            "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        res=[]

        def lettercombinations(index,curr):
            if index==len(digits):
                res.append("".join(curr))
                return
            for i in phone[digits[index]]:
                curr.append(i)
                lettercombinations(index+1,curr)
                curr.pop()
        lettercombinations(0,[])
        return res