class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def combination2(i,num,curr,flag):
            if num==0:
                res.append(list(curr))
                return 
            if i==len(candidates) or candidates[i]>num:
                return 
            combination2(i+1,num,curr,False)
            if(i==0 or candidates[i]!=candidates[i-1] or flag):
                curr.append(candidates[i])
                combination2(i+1,num-candidates[i],curr,True)
                curr.pop()
        combination2(0,target,[],True)
        return res